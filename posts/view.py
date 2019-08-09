
from flask import abort,render_template

from posts import bp
from models.post import Post
from auth.utils import loginRequired


@bp.route("/<int:id_>")
def index(id_):	

	try:
		post = Post.query({"id":id_})[0]
	except IndexError:
		abort(404)
	return render_template("posts/post.html",post=post)



@bp.route("/create")
@loginRequired
def create():
	return "ok"

	
