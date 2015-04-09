import os
import sys

from pdtTools.database import init_db, db_session
from pdtTools.models import User

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
selection_file = os.path.join(PROJECT_ROOT, 'selectionOn.txt')



def selectionStatus():
    return os.path.exists(selection_file)
    
def startSelection():
    open(selection_file, 'a').close()
    for user in User.query.filter(User.is_live_in==True).all():
        user.has_selected = False

    db_session.commit()
    
def stopSelection():
    os.remove(selection_file)

