import json

import phonenumbers as pn
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Boolean, Date, TypeDecorator
from werkzeug import generate_password_hash, check_password_hash

from pdtTools.database import Base


class PhoneNumber(TypeDecorator):

    impl = String

    def process_bind_param(self, value, dialect):
        number = pn.parse(value, 'US')
        return pn.format_number(number, pn.PhoneNumberFormat.NATIONAL)

    def process_result_value(self, value, dialect):
        return pn.parse(value, 'US')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    phone = Column(PhoneNumber(11))

    password_hash = Column(String(54))
    is_admin = Column(Boolean)

    def __init__(self, **kwargs):
        self.is_admin = False  # can be overridden in kwargs
        for attr in kwargs:
            if attr == 'password_hash':
                self.setPassword(kwargs[attr])  # store password as a hash
            else:
                setattr(self, attr, kwargs[attr])  # normal attributes

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def setPassword(self, password):
        'Hash a given password and store it'
        self.password_hash = generate_password_hash(password)
        
    def checkPassword(self, password):
        'Check the given password (hash) against the stored hash'
        return check_password_hash(self.password_hash, password)
        


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    workers = Column(String(128))

    def addWorker(self, worker):
        if self.workers:
            workers = json.loads(self.workers)  # load saved array of ints
            workers.append(worker.id)  # add worker id
        else:
            workers = [worker.id, ]  # initialize array and add worker id
        
        self.workers = json.dumps(workers)  # update workers json field

    def getWorkers(self):
        worker_ids = json.loads(self.workers)  # load saved array of ints
        workers = []  # array of User objects
        for worker_id in worker_ids:
            worker = User.query.filter(User.id == worker_id).first()
            if worker:  # since id does not necessarily exist in db
                workers.append(worker)

        return workers
