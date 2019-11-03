import os

from flask import render_template,request,url_for,redirect,flash

from views.user import bp
from views.auth.utils import loginRequired,getCurrentUser
from views.user.utils import updateUser,extensionIsAllowed
from config import Config


@bp.route("/",methods=["POST","GET"])
@loginRequired
def profile():
    if request.method == "POST":
        user = getCurrentUser()

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        pic = request.files["profileImg"]

        if not extensionIsAllowed(pic):
            flash(f"the allowed extensions are {' , '.join(Config.ALLOWED_EXTENSIONS)} !")
            return redirect(url_for(".profile"))

        updateUser(user,username=username,email=email,password=password,pic=pic)

        return redirect(url_for(".profile"))

    return render_template("user/profile.html",user=getCurrentUser())
