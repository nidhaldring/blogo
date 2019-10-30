
from flask import render_template

from views.user import bp
from views.auth.utils import loginRequired,getCurrentUser

@bp.route("/")
@loginRequired
def profile():
    return render_template("user/profile.html",user=getCurrentUser())
