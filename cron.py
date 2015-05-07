from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job

'''
This script should be run by a cron job every morning.
It will text the people who have kitchen duty that day and remind them to do their job.
If they reply, the flask server will handle the group message functionality.'''

def text(phone, message):
    print('Sending message to %s' % phone)
    print('"%s"' % message)

def remind(worker, job):
    '''Send worker a personalized reminder of kitchen duty.'''
    body = 'Hey %s, you have kitchen duty today with the following people:\n' % worker.name
    for coworker in job.getWorkers():
        if coworker == worker:
            continue
        body += '\t* %s' % coworker.name
    body += '\nRespond to this message to initiate a group conversation.'
    text(worker.phone, body)
        

if __name__ == '__main__':
    job_today = Job.query.filter(Job.date == date.today()).first()
    if job_today:
        for worker in job_today.getWorkers():
            remind(worker, job_today)
            print('')
