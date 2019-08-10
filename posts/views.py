
from flask import abort,render_template,request,redirect,url_for,flash

from posts import bp
from models.post import Post
from auth.utils import loginRequired,getCurrentUser
from posts.utils import getPostsDifference


@bp.route("/<int:id_>")
def index(id_):	

	try:
		post = Post.query({"id":id_})[0]
		print(post)
	except IndexError:
		abort(404)
	return render_template("posts/post.html",post=post)



@bp.route("/create",methods=["GET","POST"])
@loginRequired
def create():
	
	if request.method == "POST":
		title = request.form["title"]
		body = request.form["body"]
		post = Post(title,body,author=getCurrentUser()).insert()

		return redirect(url_for("posts.index",id_=post.id))

	return render_template("posts/create.html")



@bp.route("/edit/<int:id>",methods=["GET","POST"])
@loginRequired
def edit(id):

	try:
		post = Post.query({"id":id})[0]
		author = post.author
	except IndexError:
		abort(404) # not found

	if author == getCurrentUser():
		if request.method == "POST":
			newData = {}

			body = request.form["body"]
			if body != post.body:
				newData["body"] = body

			title = request.form["title"]
			if title != post.title:
				newData["title"] = title

			post.update(newData)

			flash("post was updated sucessfully !")
			return redirect(url_for("posts.index",id_=post.id))

		return render_template("posts/edit.html")

	abort(403) #forbidden

	
