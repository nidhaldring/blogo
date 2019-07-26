
import pymysql
from config import Config 


class UserNotRegistredException(Exception):

	def __init__(self):

		self.message = "The user is not yet registered on the db"



class User:

	'''
	manages a user in db
	'''

	DB = dict(db=Config.DB_NAME,user="root",password="root",host="localhost")
	TABLE = "users"

	def __init__(self,username,password,email,id_=None):

		self.id = id_
		self.username = username
		self.password = password
		self.email = email 


	def register(self):

		conn = pymysql.connect(**self.DB)
		sql = f"insert into {self.TABLE}(username,password,email) values(%s,%s,%s)"
		cursor = conn.cursor()

		cursor.execute(sql,(self.username,self.password,self.email))

		conn.commit()
		conn.close()

		# set id to the current value on the table 
		# so delete op can be possible from now on
		self.id = int(self.searchByEmail(self.email).id)

	def delete(self):

		if self.id is None:
			
			raise UserNotRegistredException() 

		conn = pymysql.connect(**self.DB)
		sql = f"delete from {self.TABLE} where id=%s"
		cursor = conn.cursor()

		cursor.execute(sql,(self.id,))

		conn.commit()
		conn.close()



	@classmethod
	def _searchByAttribute(cls,name,value):

		conn = pymysql.connect(**cls.DB)
		cursor = conn.cursor()
		sql = f"select * from {cls.TABLE} where {name}=%s"

		cursor.execute(sql,(value,))
		res = cursor.fetchone()

		cursor.close()
		conn.close()

		return cls(res[1],res[2],res[3],res[0]) if res else None
#               userusername ,password ,email,id


	@classmethod
	def searchByEmail(cls,email):
		return cls._searchByAttribute("email",email)

	@classmethod
	def searchByID(cls,id_):
		return cls._searchByAttribute("id",id_)


	# for debugging purposes
	def __str__(self):
		return f"{self.username} [{self.id}]"