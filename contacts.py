import csv
from shell import User, db_session

with open('contacts.csv', 'rb') as fh:
    reader = csv.reader(fh)
    for name, number in reader:
        number = number.strip()
        if not number:
            print('%s is missing a phone number' % name)
            continue
        user = User(name=name, phone=number)
        db_session.add(user)
        db_session.flush()
        print('Added %s' % name)
    db_session.commit()
