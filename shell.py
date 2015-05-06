from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

if __name__ == '__main__':
    luis = User(name='Luis', phone='206-478-4652')
    tyler = User(name='Tyler', phone='4259714405')
    michael = User(name='Michael', phone='206 520 1234')

    db_session.add(luis)
    db_session.add(tyler)
    db_session.add(michael)
    db_session.flush()

    print 'Users: %r' % User.query.all()

    job = Job()
    job.date = date.today()
    job.addWorker(luis)
    job.addWorker(tyler)
    
    db_session.add(job)
    db_session.flush()

    print 'Workers: %r' % job.getWorkers()

    db_session.commit()
else:
    job = Job.query.filter(Job.id == 1).first()
    michael = User.query.filter(User.name == 'Michael').first()

