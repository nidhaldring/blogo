
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

		# fetch the current user from db 
		# and set the id  
		# so delete op can be possible from now on
		currentUser = self.query(dict(email=self.email))[0]
		self.id = int(currentUser.id)

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
		return f"{self.username} [{self.id}]"