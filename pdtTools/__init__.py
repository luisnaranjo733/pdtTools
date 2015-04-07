from flask import Flask

app = Flask(__name__)

# Import the view module after the application object is created.
import pdtTools.views
from pdtTools.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



