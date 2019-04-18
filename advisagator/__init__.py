""" Application package initializer """
import flask
from . import index
from . import db_connect
from . import students
from . import teachers
from . import login


# main flask instance
app = flask.Flask(__name__)
