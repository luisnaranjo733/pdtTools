'''
This cron job will run once a day, and remind users of their upcoming chaperone
obligations (4)
'''
import os
import sys
from datetime import datetime
path = os.path.join('/home/luis/Documents', 'pdt')
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pdt.settings'

from roomDoctor.models import *

room = Room.objects.get(pk=1)
person = Person.objects.get(pk=1)
