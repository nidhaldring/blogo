
from flask import (request,render_template,redirect,url_for)

from auth import bp
from models.user import User
from utils.loginManager import loginUser,getCurrentUser



@bp.route("/register",methods=["POST","GET"])
def register():

	if request.method == "POST":

		u = User(request.form["username"],
			request.form["password"],
			request.form["email"]
			)
		u.register()
		loginUser(u)

		return redirect(url_for("auth.index"))

	return render_template("auth/register.html")



# TODO: delete this later
@bp.route("/")
def index():

	return str(getCurrentUser())













