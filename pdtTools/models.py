from sqlalchemy import Column, Integer, String
from werkzeug import generate_password_hash, check_password_hash
from pdtTools.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password_hash = Column(String(54))
    # bond number
    # house points

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
