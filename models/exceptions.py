
# exceptions for model

class ModelAlreadyInsertedException(Exception):pass

class ModelNotInsertedException(Exception):pass

class ModelUniqueConstraintException(Exception):pass

# exceptions for user class

class UserAlreadyRegistredException(ModelAlreadyInsertedException):
	def __init__(self):
		self.message = "The user is already registred !"

class UserNotRegistredException(ModelNotInsertedException):
	def __init__(self):
		self.message = "The user is not yet registered on the db"

class EmailAlreadyExistsException(ModelUniqueConstraintException):
	def __init__(self):
		self.message = "This email is already in use !"

# exceptions fro post clas

class PostAlreadyInsertedException(ModelAlreadyInsertedException):
	def __init__(self):
		self.message = "This post is already inserted on the db !"

class PostNotInsertedException(ModelNotInsertedException):
	def __init__(self):
		self.message = "This post is not inserted on the db !"

class PostRequiredArgumentMissingException(Exception):
	def __init__(self,missingArg):
		self.message = f"You must provide {missingArg} !"

class PostAuthorDoesNotExistException(Exception):
	def __init__(self):
		self.message = "The post author does not exist !"

