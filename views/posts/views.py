
from flask import abort,render_template,request,redirect,url_for,flash

from views.posts import bp
from models.post import Post
from views.auth.utils import loginRequired,getCurrentUser


@bp.route("/<int:id>")
def index(id):
	try:
		post = Post.query().filter_by(_id=id).one()
	except:
		flash("post not found !")
		abort(404)
	return render_template("posts/post.html",post=post)


@bp.route("/create",methods=["GET","POST"])
@loginRequired
def create():
	if request.method == "POST":
		title = request.form["title"]
		body = request.form["body"]
		post = Post(
			title=title,
			body=body,
			userId=getCurrentUser().id
		)
		post.insert()
		return redirect(url_for("posts.index",id=post.id))

	return render_template("posts/create.html")



@bp.route("/edit/<int:id>",methods=["GET","POST"])
@loginRequired
def edit(id):
	try:
		post = Post.query().filter_by(_id=id).one()
	except:
		flash("post not found !")
		abort(404) #not found

	author = post.user
	if author.id == getCurrentUser().id:
		if request.method == "POST":
			post.body = request.form["body"]
			post.title = request.form["title"]
			post.insert()
			flash("post was updated sucessfully !")
			return redirect(url_for("posts.index",id=post.id))
		return render_template("posts/edit.html",post=post)
	abort(403) #forbidden
