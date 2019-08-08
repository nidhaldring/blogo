


# mock objects

class MockQueryMaker:
	def __init__(self):
		self.table = ""
	def makeInsertQuery(self,data):pass 
	def makeDeleteQuery(self,cond):pass 
	def makeUpdateQuery(self,data,cond):pass 
	def makeSearchQuery(self,cond):pass
#

