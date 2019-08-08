

from models.exceptions import ModelAlreadyInsertedException,ModelNotInsertedException,ModelUniqueConstraintException

class Model:

	'''base class for all models'''

	dbManager = None 
	queryMaker = None
		
	def __init__(self,data:dict,_id=None):

		self.data = data 
		self._id = _id

	@property
	def id(self):
		return self._id
	
	@id.setter
	def id(self,v):
		raise AttributeError("Can't set id !")


	def insert(self):

		if self._id is not None:
			raise ModelAlreadyInsertedException()

		sql = self.queryMaker.makeInsertQuery()

		try:
			self.dbManager.execute(sql)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise ModelUniqueConstraintException()
		# set the id
		self._id = self.dbManager.execute(f"select max(id) from {self.queryMaker.table};")[0][0]

		return self

	def delete(self):

		if self._id is None:
			raise ModelNotInsertedException()

		sql = self.queryMaker.makeDeleteQuery({"id":self.id})
		self.dbManager.execute(sql)
		self._id = None

		return self


	def update(self,newData:dict):

		if self._id is None:
			raise ModelNotInsertedException()

		# update the current object
		self.__dict__.update(newData)

		sql = self.queryMaker.makeUpdateQuery(newData,{"id":self.id})
		
		try:
			self.dbManager.execute(sql)
		except pymysql.err.IntegrityError as e:
			if e.args[0] == 1062:
				raise ModelUniqueConstraintException()

		return self


	def __getattr__(self,key):

		return self.data[key]

	def __eq__(self,other):

		return self.data == other.data and self.id == other.id

	@classmethod
	def _search(cls,cond:dict):

		return cls.dbManager.execute(cls.queryMaker.makeSearchQuery(cond))


