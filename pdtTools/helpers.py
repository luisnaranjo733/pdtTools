import os
import platform
from functools import wraps

from twilio.rest import TwilioRestClient
import phonenumbers as pn
import flask


# Twilio initialization
# ==================================================================================


# Find these values at https://twilio.com/user/account
account_sid = "AC704c52f848ac4a38e1c79c261fb5be1a"

dist = platform.dist()[0]
home = os.path.expanduser('~')

if dist == 'centos':
    path = os.path.join(home, 'webapps/phidelttools/pdtTools/token.txt')
else:
    path = os.path.join(home, 'projects/pdtTools/token.txt')

with open(path, 'r') as fh:
    auth_token = fh.read().strip()
    
client = TwilioRestClient(account_sid, auth_token)


def sms(phone, message):
    '''Send a text message to the given phone number (pn object).'''

    phone = pn.format_number(phone, pn.PhoneNumberFormat.INTERNATIONAL)
    print('Sending message to %s' % phone)
    print('"%s"' % message)
    
    return client.messages.create(to=phone, from_="+16198318787", body=message)

# ==================================================================================

def relay_message(worker, coworkers, message):
    '''Relay a message from worker to all coworkers except for worker.

    This code is used for mediating group chat over sms'''
    for coworker in coworkers:
        if coworker == worker: # don't want to message the person sending the message
            continue
        
        sms(coworker.phone, '%s: %s' % (worker.name, message))


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print flask.session
        print f
        if not flask.session.get('logged_in'):
            print "USER NOT LOGGED IN"
            return flask.redirect(flask.url_for('login', next=flask.request.url))
        return f(*args, **kwargs)
    return decorated_function

