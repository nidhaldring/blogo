

from flask import render_template

from views.auth.utils import getCurrentUser
from views.home import bp
from models.post import Post

@bp.route("/")
def index():
	return render_template("home/index.html",posts=Post.query().all(),user=getCurrentUser())
