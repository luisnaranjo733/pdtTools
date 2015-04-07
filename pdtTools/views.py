from flask import render_template, request, flash
from flask import redirect, url_for, session
from pdtTools import app
from pdtTools.models import User

@app.route('/')
def cover_home():
    #return render_template('base.html')
    return render_template('cover_home.html', home_active='active')
    
@app.route('/features')
def cover_features():
    return render_template('cover_features.html', features_active='active')
    
@app.route('/contact')
def cover_contact():
    return render_template('cover_contact.html', contact_active='active')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    email = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter(User.email == email).first()
        if user:
            if user.check_password(password):
                flash("Succesful authentication", 'success')
                session['logged_in'] = user.name
                return redirect(url_for('cover_home'))
        else:
            error = 'Invalid username/password'
    params = {
        'error': error,
        'email': email,
        'login_active': 'active'
    }
    return render_template('login.html', **params)
    
@app.route('/logout')
def logout():
    session['logged_in'] = ''
    return redirect(url_for('cover_home'))
