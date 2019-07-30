

import unittest

import pymysql
from werkzeug.security import check_password_hash

from models.user import *


User.DB_CON = dict(db="test",user="root",password="root",host="localhost")


class TestUser(unittest.TestCase):

	def setUp(self):

		self.u = User("n","n","g@g.com")

	def tearDown(self):

		conn = pymysql.connect(**User.DB_CON)
		cursor = conn.cursor()
		cursor.execute("delete from users;")
		conn.commit()
		conn.close()

	
	def test_delete_raises_when_deleting_unregistred_user(self):

		self.assertRaises(UserNotRegistredException,self.u.delete)

	def test_register_update_db(self):

		self.u.register()
		u = User.query({"email":self.u.email})

		# assert registration
		self.assertNotEqual(u,[])

		# assert data is retreived correctly
		u = u[0]
		self.assertEqual(u.username,"n")
		self.assertTrue(check_password_hash(u.password,"n"))		
		self.assertEqual(u.email,"g@g.com")

	def test_register_raises_when_reregistering_user(self):

		# assert register method works only on unregistred users
	
		self.u.register()
		self.assertRaises(UserAlreadyRegistredException,self.u.register)

	def test_register_raises_when_registering_with_duplicate_email(self):

		self.u.register()

		# assert no duplicate emails are allowed on registration
		self.assertRaises(EmailAlreadyExistsException,User("n","n","g@g.com").register)

	def test_delete_update_db(self):

		# assert deletion 
		self.u.register()
		self.u.delete()
		self.assertEqual(User.query({"email":self.u.email}),[])

	def test_update_raises_when_updating_unregistred_user(self):


		newData = {"email":"ff@ff.com","password":"555"}

		# assert update only works on registred users
		self.assertRaises(UserNotRegistredException,self.u.update,newData)

	def test_update_change_values_inplace_and_on_db(self):

		newData = {"email":"ff@ff.com","password":"555"}

		self.u.register().update(newData)

		for key,v in newData.items():	
			if key != "password":
				self.assertEqual(getattr(self.u,key),v)
			else:
				self.assertTrue(check_password_hash(self.u.password,"555"))


	def test_update_raises_when_updating_with_a_duplicate_email(self):

		# assert no duplicate emails are allowed on update
		newData = {"email":self.u.email}
		self.u.register()
		u = User("f","f","f").register()

		self .assertRaises(EmailAlreadyExistsException,u.update,newData)


