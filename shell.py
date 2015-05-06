from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

job = Job.query.filter(Job.id == 1).first()

if not job:
    job = Job()
    job.date = date.today()
    db_session.add(job)
    db_session.commit()

users_data = [
    {
        'name': 'Luis',
        'phone': '206 478 4652',
    },

    {
        'name': 'Tyler',
        'phone': '425 971 4405',
    },

    {
        'name': 'Michael',
        'phone': '206 501 5201',
    },
]

if User.query.count() < 3:
    for user_data in users_data:
        user = User(**user_data)
        user.setPassword('test')
        db_session.add(user)
        db_session.commit()

        job.addWorker(user)
        db_session.commit()
        
print job.getWorkers()


