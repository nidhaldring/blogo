
from abc import ABC,abstractmethod

import pymysql

from models.utils import executeSQL
from models.exceptions import ModelAlreadyInsertedException,ModelNotInsertedException


class Model(ABC):

	'''abstract class to map data to db'''
	
	def __init__(self,dbCon:dict,table,data:dict,_id=None):


		self.dbCon = dbCon
		self.table = table
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

		sql = f"insert into {self.table}"
		sql += "(" + " , ".join(self.data.keys()) +")"
		sql += " values(" + " , ".join([f"'{i}'" for i in self.data.values()]) + ")"

		executeSQL(self.dbCon,sql)

		# set the id
		self._id = self.query({"email":self.email})[0].id

		return self

	def delete(self):

		if self._id is None:
			raise ModelNotInsertedException()

		sql = f"delete from {self.table} where  id={self._id}"
		executeSQL(self.dbCon,sql)

		self._id = None

		return self


	def update(self,newData:dict):

		if self._id is None:
			raise ModelNotInsertedException()

		# update the current object
		self.__dict__.update(newData)

		sql = f"update {self.table} set "
		sql +=  " , ".join(["{} = '{}' ".format(i,j) for i,j in newData.items()])
		sql += f"where id = {self._id}"

		executeSQL(self.dbCon,sql)

		return self


	@abstractmethod
	def query(self,cond:dict):pass


	def __getattr__(self,key):

		return self.data[key]



