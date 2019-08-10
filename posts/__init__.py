

from flask import Blueprint

bp = Blueprint("posts",__name__)

from posts.views import *