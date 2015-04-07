from flask import render_template, request, flash
from flask import redirect, url_for
from pdtTools import app
from pdtTools.models import User

@app.route('/')
def cover_home():
    return render_template('cover_home.html')
    
@app.route('/features')
def cover_features():
    return render_template('cover_features.html')
    
@app.route('/contact')
def cover_contact():
    return render_template('cover_contact.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter(User.email == email).first()
        if user:
            if user.check_password(password):
                flash("Succesful authentication")
                return redirect(url_for('cover_home'))
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)
    

