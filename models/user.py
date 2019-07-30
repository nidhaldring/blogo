
from werkzeug.security import generate_password_hash
import pymysql

from config import Config 
from models.utils import query,insert,delete,update
from models.exceptions import UserAlreadyRegistredException,UserNotRegistredException,EmailAlreadyExistsException
					

class User:

	'''manages a user in db'''

	DB_CON = dict(db=Config.DB_NAME,user="root",password="root",host="localhost")
	TABLE = "users"

	# id_ should only be set internally
	def __init__(self,username,password,email,id_=None):

		self._id = id_
		self.username = username
		self.password = password
		self.email = email 


	@property
	def id(self):
		return self._id
	
	@id.setter
	def id(self,v):
		raise AttributeError("Can't set id !")
	
	@classmethod
	def query(cls,cond:dict) -> list:

		res = query(cls.DB_CON,cls.TABLE,cond)
		return [cls(row[1],row[2],row[3],row[0]) for row in res] 


	def register(self):

		if self._id is not None:
			raise UserAlreadyRegistredException()

		try:
			data = dict(username=self.username,password=generate_password_hash(self.password),email=self.email)
			insert(self.DB_CON,self.TABLE,data)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e

		# set the id  
		# so delete/update op can be possible from now on
		currentUser = self.query(dict(email=self.email))[0]
		self._id = int(currentUser.id)

		return self

	def delete(self):

		if self._id is None:	
			raise UserNotRegistredException() 

		delete(self.DB_CON,self.TABLE,{"id":self._id})

		self._id = None

		return self

	def update(self,newData):

		'''returns the new updated user'''

		if self.id is None:
			raise UserNotRegistredException()

		# hash the password
		if "password" in newData:
			newData.update({"password":generate_password_hash(newData["password"])})

		# update the current object
		self.__dict__.update(newData)

		#update db
		try:
			update(self.DB_CON,self.TABLE,self._id,newData)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e


		return self	


	# for debugging purposes
	def __repr__(self):
		return f"{self.username} [{self._id}]"