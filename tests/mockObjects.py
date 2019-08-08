


# mock objects

class MockDbManager:
	def execute(self,sql):
		return [("1","1","1","1")]

class MockQueryMaker:
	def __init__(self):
		self.table = ""
	def makeInsertQuery(self):pass 
	def makeDeleteQuery(self,cond):pass 
	def makeUpdateQuery(self,data,cond):pass 
	def makeSearchQuery(self,cond):pass
#

