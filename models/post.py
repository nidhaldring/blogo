

from models.model import Model
from models.user import User
from models.utils.dbManager import DbManager 
from models.utils.sqlQueryMaker import SQLQueryMaker 
from models.exceptions import *
from config import Config


class Post(Model):

	dbManager = DbManager()
	queyMaker = SQLQueryMaker(Config.POSTS_TABLE)

	def __init__(self,title,body,author,_id=None):

		super().__init__(dict(title=title,body=body),_id)
		self.author = author


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

	@classmethod
	def query(cls,cond):

		res = cls._search(cond)
		return [cls(row[1],row[2],row[3],row[0]) for row in res]

