

from flask import session

from models.user import User,UserNotRegistredException


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


def logout_user():

	session.clear()
	global currentUser
	currentUser = None



