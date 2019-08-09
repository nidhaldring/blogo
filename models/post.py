

from models.model import Model
from models.user import User
from models.utils.dbManager import DbManager 
from models.utils.sqlQueryMaker import SQLQueryMaker 
from models.exceptions import *
from config import Config


class Post(Model):

	dbManager = DbManager()
	queryMaker = SQLQueryMaker(Config.POSTS_TABLE)

	def __init__(self,title,body,*,authorID=None,author=None,_id=None):

		if not author and not authorID:
			raise PostRequiredArgumentMissingException()

		super().__init__(dict(title=title,body=body,authorID=authorID),_id)
		self._author = author

	@property
	def author(self):
		if not self._author:
			self._author = User.query({"id":self.authorID})[0]
		return self._author
	

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
			return super().update(cond)
		except ModelNotInsertedException:
			raise PostNotInsertedException()

	@classmethod
	def query(cls,cond):

		return [cls(row[1],row[2],authorID=row[3],_id=row[0]) for row in cls._search(cond)]

