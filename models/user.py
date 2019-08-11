
from werkzeug.security import generate_password_hash

from config import Config 
from models.model import Model
from models.utils.dbManager import DbManager
from models.utils.sqlQueryMaker import SQLQueryMaker
from models.exceptions import *
					


class User(Model):

	'''manages a user in db'''

	dbManager = DbManager()
	queryMaker = SQLQueryMaker(table=Config.USERS_TABLE)

	# id_ should only be set internally
	def __init__(self,username,password,email,_id=None):

		data = dict(username=username,password=password,email=email)
		super().__init__(data=data,_id=_id)
	

	def register(self):

		try:
			self.data["password"] = generate_password_hash(self.password)
			return super().insert()
		except ModelUniqueConstraintException:			
				raise EmailAlreadyExistsException()
		except ModelAlreadyInsertedException:
			raise UserAlreadyRegistredException()

	def delete(self):

		try:
			return super().delete()
		except ModelNotInsertedException:
			raise UserNotRegistredException()

	def update(self,newData):

		# hash the password
		if "password" in newData:
			newData.update({"password":generate_password_hash(newData["password"])})
		
		try:
			return super().update(newData)
		except ModelUniqueConstraintException:
			raise EmailAlreadyExistsException()
		except ModelNotInsertedException:
			raise UserNotRegistredException()


	@classmethod
	def query(cls,cond:dict,limit=None) -> list:

		return [cls(row[1],row[2],row[3],_id=row[0]) for row in cls._search(cond,limit)] 

	# for debugging purposes
	def __repr__(self):
		return f"{self.username} [{self._id}]"
