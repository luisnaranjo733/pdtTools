from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

user = User.query.filter(User.id == 1).first()

if not user:
    user = User()
    user.name = 'Luis'
    user.email = 'luisnaranjo733@gmail.com'
    user.phone = '206-478-4652'
    user.setPassword('test')
    db_session.add(user)
    db_session.commit()

job = Job.query.filter(Job.id == 1).first()

if not job:
    job = Job()
    job.addWorker(user)
    job.date = date(2015, 5, 15)
    db_session.add(job)
    db_session.commit()

