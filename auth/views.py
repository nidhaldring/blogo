
from flask import (request,render_template,redirect,url_for,flash)

from auth import bp
from models.user import User
from utils.loginManager import loginUser,getCurrentUser,logoutUser



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
		u.register()
		loginUser(u)

		return redirect(url_for("auth.index"))

	return render_template("auth/register.html")




@bp.route("/login",methods=["POST","GET"])
def login():

	if getCurrentUser() is not None:

		flash("You're already logged in !")
		return redirect(url_for("auth.index"))

	if request.method == "POST":
			
		username = request.form["username"]
		password = request.form["password"]
		res = User.query({"username":username,"password":password})
		u = res[0]

		if not u:
			flash("incorrect login !")
			return redirect(url_for("auth.index"))
		
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













