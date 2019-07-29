


# exceptions for user class

class UserAlreadyRegistredException(Exception):
	def __init__(self):
		self.message = "The user is already registred !"

class UserNotRegistredException(Exception):
	def __init__(self):
		self.message = "The user is not yet registered on the db"

class EmailAlreadyExistsException(Exception):
	def __init__(self):
		self.manage = "This email is already in use !"

#

