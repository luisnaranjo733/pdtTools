from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

if __name__ == '__main__':
<<<<<<< HEAD
    if len(argv) == 1:
        print('Create is -c')
        print('List is -c')
        print('Delete is -d')
        exit(1)

    flag = argv[1]

    if flag == '-c':
        luis = User(name='Luis', phone='206-478-4652')
        tyler = User(name='Tyler', phone='4251111111')
        michael = User(name='Michael', phone='206 520 1234')

        db_session.add(luis)
        #db_session.add(tyler)
        db_session.add(michael)
        db_session.flush()

        job = Job()
        job.date = date(2015, 5, 6)
        job.addWorker(luis)
        job.addWorker(michael)
        
        db_session.add(job)
=======
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
>>>>>>> b01343d615fe92fdf1a79fbc6e2766e5ece84d95

        db_session.commit()
    elif flag == '-l':
        print('Users:')
        for user in User.query.all():
            print('\t%r (%s)' % (user, user.phone))
        print('')

        print('Jobs:')
        for job in Job.query.all():
            print('\tDate: %r' % job.date)
            print('\tWorkers: %r' % [worker for worker in job.getWorkers()])
            print('')
    elif flag == '-d':
        User.query.delete()
        Job.query.delete()
        db_session.commit()
