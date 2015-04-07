from flask import render_template, request
from pdtTools import app
from pdtTools.models import User

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    print request.method
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter(User.email == email).first()
        if user:
            if user.check_password(password):
                return 'Authed'
            else:
                return 'Wrong password'
        else:
            return 'user does not exist'
        
    return 'get'
