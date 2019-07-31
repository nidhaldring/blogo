

from models.model import Model
from models.user import User
from models.utils import query
from models.exceptions import *


class Post(Model):

	DB_CON = dict(host="localhost",db="test",user="root",password="root")
	TABLE = "posts"


	def __init__(self,title,body,authorID,_id=None):

		data = dict(title=title,body=body,authorID=authorID)
		super().__init__(self.DB_CON,self.TABLE,data,_id)

	
	@classmethod
	def query(cls,cond):

		res = query(cls.DB_CON,cls.TABLE,cond)
		return [cls(row[1],row[2],row[3],row[0]) for row in res]

	def insert(self):

		try:
			return super().insert()
		except ModelAlreadyInsertedException:
			raise PostAlreadyInsertedException()


	def delete(self):

		try:
			return super().delete()
		except ModelNotInsertedException:
			raise PostNotInsertedException()

	def update(self,cond:dict):
			
		try:
			super().update(cond)
		except ModelNotInsertedException:
			raise PostNotInsertedException()
