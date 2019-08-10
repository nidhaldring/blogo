
from flask import (request,render_template,redirect,url_for,flash)
from werkzeug import check_password_hash

from views.auth import bp
from models.user import User,EmailAlreadyExistsException
from views.auth.utils import loginUser,getCurrentUser,logoutUser,loginRequired



@bp.route("/register",methods=["POST","GET"])
def register():

	if getCurrentUser() is not None:

		flash("You're already registred !")	
		return redirect(url_for("auth.index"))

	if request.method == "POST":

		u = User(request.form["username"],
			request.form["password"],
			request.form["email"]
			)

		try:
			u.register()
		except EmailAlreadyExistsException as e:
			flash(e.message)
			return redirect(url_for("auth.index"))
			
		loginUser(u)

		return redirect(url_for("auth.index"))

	return render_template("auth/register.html")




@bp.route("/login",methods=["POST","GET"])
def login():

	if getCurrentUser() is not None:

		flash("You're already logged in !")
		return redirect(url_for("auth.index"))

	if request.method == "POST":
			
		email = request.form["email"]
		password = request.form["password"]
		res = User.query({"email":email})
		u = res[0] if res else None

		if not u or not check_password_hash(u.password,password):
			flash("incorrect login !")
			return redirect(url_for("auth.login"))
		
		loginUser(u)
		flash(f"welcome {u.username} !")
		return redirect(url_for("auth.index"))

	return render_template("auth/login.html")



@bp.route("/logout")
def logout():

	logoutUser()
	return redirect(url_for("auth.index"))


# TODO: delete this later
@bp.route("/")
def index():
	return str(getCurrentUser())
