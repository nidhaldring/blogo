

from flask import Blueprint

bp = Blueprint("user",__name__)

from views.user.views import *
