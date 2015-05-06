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

@app.route('/kitchen_bot', methods=['POST'])
def kitchenBot():
    phone = flask.request.form['phone']
    phone = pn.parse(phone, 'US')
    message = flask.request.form['message']
    for worker in User.query.all():
        if worker.phone == phone:
            return worker.name
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
