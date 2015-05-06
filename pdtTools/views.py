from datetime import date

import flask
import phonenumbers as pn
from pdtTools import app
from pdtTools.models import User, Job

@app.route('/')
def home():
    return flask.render_template('home.html')
    
@app.route('/kitchen_duty')
def kitchenDuty():
    return flask.render_template('kitchen_duty.html', contact_active='active')

def message_coworkers(coworkers, worker):
    print repr(coworkers)
    for coworker in coworkers:
        if coworker == worker:
            continue
        print coworker.id

@app.route('/kitchen_bot', methods=['POST'])
def kitchenBot():
    phone = flask.request.form['phone']
    phone = pn.parse(phone, 'US')  # NEED ERROR HANDLING - SMS RESPONSE
    message = flask.request.form['message']

    # today's job if it exists
    today = Job.query.filter(Job.date == date.today()).first()
    if today:
        todays_workers = today.getWorkers()
        for worker in User.query.all():
            if worker.phone == phone and worker in todays_workers:
                message_coworkers(todays_workers, worker)
                return worker.name
    else:
        return 'No kitchen duty today!'
    return 'thanks'
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    params = {'login_active': 'active'}
    if flask.request.method == 'POST':
        email = flask.request.form['email']
        password = flask.request.form['password']
        
        if email:
            params['email'] = email
        
        user = User.query.filter(User.email == email).first()
        if user: # if email exists in database
            if user.checkPassword(password):
                flask.flash("Succesful authentication")
                session['logged_in'] = user.name
                return flask.redirect(url_for('cover_home'))
                
        flask.flash('Invalid username/password')  # this will only happen if auth failed

    return flask.render_template('login.html', **params)
    
@app.route('/logout')
def logout():
    session['logged_in'] = ''
    return flask.redirect(flask.url_for('cover_home'))
