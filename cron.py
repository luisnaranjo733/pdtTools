from sys import argv
from datetime import date

from pdtTools.database import init_db, db_session
from pdtTools.models import User, Job
from pdtTools.sms import sms


def remind(worker, job):
    '''Send worker a personalized reminder of kitchen duty.'''
    body = 'Hey %s, you have kitchen duty today with the following people:\n' % worker.name
    for coworker in job.getWorkers():
        if coworker == worker:
            continue
        body += '    * %s' % coworker.name
    body += '\nRespond to this message to initiate a group conversation.'
    sms(worker.phone, body)
        


if __name__ == '__main__':
    job_today = Job.query.filter(Job.date == date.today()).first()
    if job_today:
        for worker in job_today.getWorkers():
            remind(worker, job_today)
            #print('')
