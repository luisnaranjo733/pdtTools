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
    person = Person.objects.get(email="luisnaranjo733@gmail.com")
except:
    print 'Created a person!'
    luis = Person.objects.create_user("luisnaranjo733@gmail.com", password='test')
    luis.setName("Luis")
    luis.setPoints(30)
    
try:
    person = Person.objects.get(email="stan@gmail.com")
except:
    print 'Created another person!'
    stan = Person.objects.create_user("stan@gmail.com", password='test')
    stan.setName("Stan")
    stan.setPoints(50)
    
    
try:
    person = Person.objects.get(email="nathan@gmail.com")
except:
    print 'Created another person!'
    nathan = Person.objects.create_user("nathan@gmail.com", password='test')
    nathan.setName("Nathan")
    nathan.setPoints(40)
    
    
