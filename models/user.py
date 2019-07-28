
import pymysql
from werkzeug.security import generate_password_hash

from config import Config 


# exceptions

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


class User:

	'''
	manages a user in db
	'''

	DB = dict(db=Config.DB_NAME,user="root",password="root",host="localhost")
	TABLE = "users"

	def __init__(self,username,password,email,id_=None):

		self._id = id_
		self.username = username
		self.password = password
		self.email = email 


	@property
	def id(self):
		return self._id
	

	def register(self):

		if self._id is not None:
			raise UserAlreadyRegistredException()

		conn = pymysql.connect(**self.DB)
		sql = f"insert into {self.TABLE}(username,password,email) values(%s,%s,%s)"
		args = (self.username,generate_password_hash(self.password),self.email)
		cursor = conn.cursor()

		try:
			cursor.execute(sql,args)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise EmailAlreadyExistsException()
			raise e

		conn.commit()
		conn.close()

		# fetch the current user from db 
		# and set the id  
		# so delete op can be possible from now on
		currentUser = self.query(dict(email=self.email))[0]
		self._id = int(currentUser.id)

		return self

	def delete(self):

		if self._id is None:	
			raise UserNotRegistredException() 

		conn = pymysql.connect(**self.DB)
		sql = f"delete from {self.TABLE} where id=%s"
		cursor = conn.cursor()

		cursor.execute(sql,(self._id,))

		conn.commit()
		conn.close()

		self._id = None

		return self

	@classmethod
	def query(cls,cond:dict) -> list:

		cond = " and ".join(["{} = '{}' ".format(i,j) for i,j in cond.items()])
		sql = f"select * from {cls.TABLE} where " + cond
		conn = pymysql.connect(**cls.DB)
		cursor = conn.cursor()

		cursor.execute(sql)
		res = cursor.fetchall()

		conn.close()

		return [cls(row[1],row[2],row[3],row[0]) for row in res] 


	# for debugging purposes
	def __str__(self):
		return f"{self.username} [{self._id}]"