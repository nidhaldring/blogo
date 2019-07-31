
from werkzeug.security import generate_password_hash
import pymysql

from config import Config 
from models.model import Model
from models.utils import query
from models.exceptions import *
					

class User(Model):

	'''manages a user in db'''

	DB_CON = dict(db=Config.DB_NAME,user="root",password="root",host="localhost")
	TABLE = "users"

	# id_ should only be set internally
	def __init__(self,username,password,email,_id=None):

		data = dict(username=username,password=password,email=email)
		super().__init__(dbCon=self.DB_CON,table=self.TABLE,data=data,_id=_id)
	

	@classmethod
	def query(cls,cond:dict) -> list:

		res = query(cls.DB_CON,cls.TABLE,cond)
		return [cls(row[1],row[2],row[3],row[0]) for row in res] 


	def register(self):

		try:
			self.data["password"] = generate_password_hash(self.password)
			return super().insert()
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e
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
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e
		except ModelNotInsertedException:
			raise UserNotRegistredException()


	# for debugging purposes
	def __repr__(self):
		return f"{self.username} [{self._id}]"