
# exceptions for model

class ModelAlreadyInsertedException(Exception):pass

class ModelNotInsertedException(Exception):pass

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

# exceptions fro post clas

class PostAlreadyInsertedException(Exception):
	def __init__(self):
		self.message = "This post is already inserted on the db !"

class PostNotInsertedException(Exception):
	def __init__(self):
		self.message = "This post is not inserted on the db !"

