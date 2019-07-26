

from flask import session

from models.user import User,UserNotRegistredException



# add support for remember me feature later 
currentUser = None 


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



