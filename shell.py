from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

if __name__ == '__main__':
    if len(argv) == 1:
        print('Create is -c')
        print('List is -c')
        print('Delete is -d')
        exit(1)

    flag = argv[1]

    if flag == '-c':
        luis = User(name='Luis', phone='206-478-4652')
        dan = User(name='Dan', phone='425 239 5949')
        michael = User(name='Michael', phone='206 520 12341')
        ep = User(name='Eric Page', phone='312 508 9500')
        justin = User(name='Justin Carpenter', phone='503 706 7882')

        db_session.add(luis)
        db_session.add(ep)
        db_session.add(justin)
        db_session.flush()

        job = Job()
        job.date = date(2015, 5, 7)
        job.addWorker(luis)
        job.addWorker(ep)
        job.addWorker(justin)
        
        db_session.add(job)

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
