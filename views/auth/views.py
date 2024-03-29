
from flask import request,render_template,redirect,url_for,flash,session
from werkzeug import check_password_hash
from sqlalchemy import exc

from views.auth import bp
from models.user import User
from views.auth.utils import *


@bp.route("/register",methods=["POST","GET"])
def register():
	if getCurrentUser() is not None:
		flash("You're already registred !")
		return redirect(url_for("home.index"))

	if request.method == "POST":
		u = User(
			username = request.form["username"],
			password = request.form["password"],
			email = request.form["email"]
		)
		try:
			u.insert()
		except exc.IntegrityError as e:
			flash("email alreay in use !")
			return redirect(url_for("auth.register"))

		loginUser(u)
		return redirect(url_for("home.index"))

	return render_template("auth/register.html")


@bp.route("/",methods=["POST","GET"])
@bp.route("/login",methods=["POST","GET"])
def login():
	if getCurrentUser() is not None:
		flash("you're already logged in !")
		return redirect(url_for("home.index"))

	if request.method == "POST":
		next = session["next"]
		session.pop("next")

		# get user infos
		email = request.form["email"]
		password = request.form["password"]

		try:
			user = User.query().filter_by(email=email).one()
		except:
			flash("login failed !")
			return redirect(url_for("auth.login"))

		if not check_password_hash(user.password,password):
			flash("login failed !")
			return redirect(url_for("auth.login"))

		loginUser(user)
		flash(f"welcome {user.username} !")
		return redirect(next) if next else redirect(url_for("home.index"))

	session["next"] = request.args.get("next")
	return render_template("auth/login.html")


@bp.route("/logout")
def logout():
	logoutUser()
	return redirect(url_for("auth.login"))
