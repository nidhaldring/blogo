
from werkzeug.security import generate_password_hash
import pymysql

from config import Config 
from models.utils import executeSQL,query
from models.exceptions import UserAlreadyRegistredException,UserNotRegistredException,EmailAlreadyExistsException
					

class User:

	'''
	manages a user in db
	'''

	DB = dict(db=Config.DB_NAME,user="root",password="root",host="localhost")
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
		raise AttributeError("can't set id !")
	

	@classmethod
	def query(cls,cond:dict) -> list:

		res = query(cls.DB,cls.TABLE,cond)
		return [cls(row[1],row[2],row[3],row[0]) for row in res] 

	def register(self):

		if self._id is not None:
			raise UserAlreadyRegistredException()

		sql = (f"insert into {self.TABLE}(username,password,email)" 
			+ f" values('{self.username}'," 
			+ f"'{generate_password_hash(self.password)}','{self.email}');")
	
		try:
			executeSQL(sql,self.DB)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e

		# fetch the current user from db 
		# and set the id  
		# so delete op can be possible from now on
		currentUser = self.query(dict(email=self.email))[0]
		self._id = int(currentUser.id)

		return self

	def delete(self):

		if self._id is None:	
			raise UserNotRegistredException() 

		sql = f"delete from {self.TABLE} where id='{self._id}'"
		executeSQL(sql,self.DB)

		self._id = None

		return self

	def update(self,newData):

		'''
		returns the new updated user
		dosn't change the user in place !
		'''

		if self.id is None:
			raise UserNotRegistredException()

		# update the current object
		self.__dict__.update(newData)

		#update db
		sql = f"update {self.TABLE} set "
		sql +=  " , ".join(["{} = '{}' ".format(i,j) for i,j in newData.items()])
		sql += f"where id = {self.id}"

		try:
			executeSQL(sql,self.DB)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e


		return self	


	# for debugging purposes
	def __str__(self):
		return f"{self.username} [{self._id}]"