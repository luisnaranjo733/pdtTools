import os, sys
from datetime import datetime
path = os.path.join('/home/luis/Documents', 'pdt')
sys.path.append(path)
path = os.path.join('C:\\Users\\Luis\\Documents\\GitHub', 'pdtTools')
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pdt.settings'

from roomDoctor.models import *

try:
    room = Room.objects.get(pk=1)
except:
    print 'Created a room!'
    room = Room()
    room.setRoomNumber(1)
    room.setIsImproved(False)
    
try:
    chore = Chore.objects.get(pk=1)
except:
    print 'Created a chore!'
    chore = Chore()
    chore.setTitle("Foyer")
    chore.setWorkerQuota(2)
    
try:
    person = Person.objects.get(pk=1)
except:
    print 'Created a person!'
    luis = Person()
    luis.setName("Luis")
    luis.setPoints(30)
    
try:
    person = Person.objects.get(pk=2)
except:
    print 'Created another person!'
    stan = Person()
    stan.setName("Stan")
    stan.setPoints(50)
    
    
try:
    person = Person.objects.get(pk=3)
except:
    print 'Created another person!'
    nathan = Person()
    nathan.setName("Nathan")
    nathan.setPoints(40)
    
    
