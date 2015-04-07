from flask import Flask
app = Flask(__name__)

# Import the view module after the application object is created.
import pdtTools.views



