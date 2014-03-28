import os
import sys
path = os.path.join('/home/luis/Documents', 'pdt')
sys.path.append(path)
path = os.path.join('C:\\Users\\Luis\\Documents\\GitHub', 'pdtTools')
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pdt.settings'

from pdt.settings import PROJECT_ROOT
from roomDoctor.models import Person

selectionFileName = 'selectionOn.txt'
selectionFile = os.path.join(PROJECT_ROOT, selectionFileName)

def selectionStatus():
    return os.path.exists(selectionFile)
    
def startSelection():
    open(selectionFile, 'a').close()
    for person in Person.objects.all():
        person.setSelected(False)
    
def stopSelection():
    os.remove(selectionFile)
    