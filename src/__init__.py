""" Application package initializer """
import flask

# main flask instance
app = flask.Flask(__name__)

# pylint: disable=wrong-import-position
from . import app
from . import login_handler
from . import database_handler
