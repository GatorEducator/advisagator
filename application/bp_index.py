import flask
import os.path

from flask import Blueprint
from flask_autoindex import AutoIndexBlueprint
from flask_autoindex import AutoIndex



auto_bp = Blueprint('auto_bp', __name__)
AutoIndexBlueprint(auto_bp, browse_root=os.path.curdir+"/uploads/")
