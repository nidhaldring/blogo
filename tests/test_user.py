

import unittest

from werkzeug.security import check_password_hash

from models.user import *
from tests.commonMockObjects import *

# mock objects
class MockDbManager:
	def execute(self,sql):
		return [("1","1","1","1")]

#

class TestUser(unittest.TestCase):

	def __init__(self,*args,**kargs):

		super().__init__(*args,**kargs)
		User.dbManager = MockDbManager()
		User.queryMaker = MockQueryMaker()
		self.u = User("h","g","h@g.com")	

	def test_delete_raises_when_deleting_unregistred_user(self):

		self.assertRaises(UserNotRegistredException,self.u.delete)


	def test_register_raises_when_reregistering_user(self):

		# assert register method works only on unregistred users
		self.u.register()
		self.assertRaises(UserAlreadyRegistredException,self.u.register)

	def test_register_set_user_id(self):

		self.u.register()
		self.assertNotEqual(self.u.id,None)

	def test_delete_set_id_to_None(self):

		self.u.register()
		self.u.delete()
		self.assertEqual(self.u.id,None)


	def test_update_raises_when_updating_unregistred_user(self):

		newData = {"email":"ff@ff.com","password":"555"}
		self.assertRaises(UserNotRegistredException,self.u.update,newData)

	def test_update_change_object_values_inplace(self):

		newData = {"email":"ff@ff.com","password":"555"}
		self.u.register().update(newData)

		for key,v in newData.items():	
			if key != "password":
				self.assertEqual(getattr(self.u,key),v)
			else:
				self.assertTrue(check_password_hash(self.u.password,"555"))

	def test_id_raises_when_changed(self):

		with self.assertRaises(AttributeError):
			self.u.id = 0


	def test_query_returns_user_with_correct_condition(self):

		u = User.query({"email":"1"})
		self.assertNotEqual(u,[])
		self.assertEqual(u[0].email,"1")
