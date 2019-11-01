import os

from flask import render_template,request,url_for,redirect

from views.user import bp
from views.auth.utils import loginRequired,getCurrentUser
from config import Config


@bp.route("/",methods=["POST","GET"])
@loginRequired
def profile():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        profileImg = request.files["profileImg"]

        u = getCurrentUser()

        profileImgPath = os.path.join(Config.UPLOAD_FOLDER,u.email + profileImg.filename)
        profileImg.save(os.path.join("static",profileImgPath))

        u.email = email
        u.username = username
        u.pic = profileImgPath
        u.insert()

        return redirect(url_for(".profile"))

    return render_template("user/profile.html",user=getCurrentUser())
