from datetime import date

import flask
import phonenumbers as pn
import twilio.twiml

from pdtTools import app
from pdtTools.models import User, Job
from pdtTools import helpers
from pdtTools.helpers import login_required
from pdtTools.database import db_session


@app.route('/')
def home():
    return flask.render_template('home.html')
    
@app.route('/kitchen_duty')
@login_required
def kitchenDuty():
    params = {
        'jobs': Job.query.filter(Job.date >= date.today()).all(),
        'workers': User.query.all(),
        'today': date.today().strftime('%m-%d-%Y')
    }
    return flask.render_template('kitchen_duty.html', **params)

@app.route('/kitchen/addJob', methods=['POST'])
@login_required
def addJob(): 
    job_date = flask.request.form.get('date')
    worker_ids = flask.request.form.getlist('workers')
    
    if job_date:  # if date passed in, convert to date object
        month, day, year = job_date.split('-')
        month = int(month)
        day = int(day)
        year = int(year)
        job_date = date(year, month, day)

    job = Job()
    job.date = job_date

    if worker_ids:  # if workers passed in, convert list of str pk's to list of ints
        worker_ids = [int(worker_id) for worker_id in worker_ids]
        for worker_id in worker_ids:
            worker = User.query.filter(User.id == worker_id).first()
            job.addWorker(worker)

    db_session.add(job)
    db_session.commit()
    return flask.redirect(flask.url_for('kitchenDuty'))

@app.route('/kitchen/delJob', methods=['POST'])
@login_required
def delJob(): 
    job_ids = flask.request.form.getlist('jobs')
    if job_ids:
        for job_id in job_ids:
            job_id = int(job_id)
            job = Job.query.filter(Job.id == job_id).first()
            db_session.delete(job)
    db_session.commit()
    return flask.redirect(flask.url_for('kitchenDuty'))


@app.route('/kitchen_bot', methods=['POST'])
def kitchenBot():
    phone = flask.request.form['From']
    try:
        phone = pn.parse(phone, 'US')
    except pn.phonenumberutil.NumberParseException:
        flask.abort(400)
    message = flask.request.form['Body']

    # today's job if it exists
    today = Job.query.filter(Job.date == date.today()).first()
    if today:  # today could be none
        todays_workers = today.getWorkers()
        for worker in User.query.all():
            if worker.phone == phone and worker in todays_workers:
                helpers.relay_message(worker, todays_workers, message)
                return worker.name

        return 'Phone not found or worker not on duty today'
    else:
        return 'No kitchen duty today!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    params = {}
    if flask.request.method == 'POST':
        email = flask.request.form.get('email')
        password = flask.request.form.get('password')
        
        params['email'] = email or ''
        
        user = User.query.filter(User.email == email).first()
        print user
        if user: # if email exists in database
            if user.checkPassword(password):
                flask.flash("Succesful authentication")
                flask.session['logged_in'] = user.name
                return flask.redirect(flask.url_for('home'))
                
        flask.flash('Invalid username/password')  # this will only happen if auth failed

    return flask.render_template('login.html', **params)
    
@app.route('/logout')
def logout():
    flask.session['logged_in'] = ''
    return flask.redirect(flask.url_for('home'))
