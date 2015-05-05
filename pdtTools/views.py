from flask import render_template, request, flash
from flask import redirect, url_for, session
from pdtTools import app
from pdtTools.models import User

@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/kitchen_duty')
def kitchenDuty():
    return render_template('kitchen_duty.html', contact_active='active')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    params = {'login_active': 'active'}
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email:
            params['email'] = email
        
        user = User.query.filter(User.email == email).first()
        if user: # if email exists in database
            if user.checkPassword(password):
                flash("Succesful authentication")
                session['logged_in'] = user.name
                return redirect(url_for('cover_home'))
                
        flash('Invalid username/password')  # this will only happen if auth failed

    return render_template('login.html', **params)
    
@app.route('/logout')
def logout():
    session['logged_in'] = ''
    return redirect(url_for('cover_home'))
