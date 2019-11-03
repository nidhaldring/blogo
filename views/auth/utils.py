
from functools import wraps

from flask import session,redirect,url_for,flash,request
from models.user import User


currentUser = None

def getCurrentUser():
	return currentUser


# add support for remember me feature later
def loginUser(user):
	if not user.id:
		raise Exception("User not Registred")
	session["_user_id"] = user.id
	global currentUser
	currentUser = user


def logoutUser():
	session.clear()
	global currentUser
	currentUser = None


def loginRequired(view):
	@wraps(view)
	def decorator(*args,**kargs):
		if getCurrentUser() is None:
			flash("you need to login to acess this page !")
			return redirect(url_for("auth.login",next=request.path))
		return view(*args,**kargs)
	return decorator
