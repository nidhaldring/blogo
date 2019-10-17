
from functools import wraps

from flask import session,abort

from models.user import User


currentUser = None

def getCurrentUser():
	return currentUser


# add support for remember me feature later
def loginUser(user):
	if not user.id:
		raise UserNotRegistredException()
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
			abort(401) # unathorized
		return view(*args,**kargs)
	return decorator
