import csv
from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

init_db()

def add_current_chapter():
    with open('contacts.csv', 'rb') as fh:
        reader = csv.reader(fh)
        for line in reader:  # name, number, password (optional)
            params = {}
            if len(line) >= 2:
                params['name'] = line[0].strip()
                params['phone'] = line[1].strip()
            if len(line) >= 3:
                params['email'] = line[2].strip()
            if len(line) >= 4:
                params['password_hash'] = line[3].strip()
            if not params['phone']:
                print('%s is missing a phone number' % name)
                continue
            #print params
            user = User(**params)
            db_session.add(user)
            db_session.flush()
            #break
            #print('Added %s' % name)
        db_session.commit()


if __name__ == '__main__':
    if len(argv) == 1:
        print('Create is -c')
        print('List is -c')
        print('Delete is -d')
        exit(1)

    flag = argv[1]

    if flag == '-c':
        add_current_chapter()

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
else:
    luis = User.query.filter(User.name == 'Luis Naranjo').first()