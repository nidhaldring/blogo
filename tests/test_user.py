

import unittest

import pymysql
from werkzeug.security import check_password_hash

from models.user import *

User.DB = dict(db="test",user="root",password="root",host="localhost")


# prepare users table for tests

conn = pymysql.connect(**User.DB)
cursor = conn.cursor()
cursor.execute("delete from users where true;")
conn.commit()
conn.close()

# end


class TestUser(unittest.TestCase):

	
	def test_register_delete_methods(self):

		u = User("n","n","g@g.com")
		self.assertRaises(UserNotRegistredException,u.delete)

		u.register()
		u = User.query({"email":"g@g.com"})

		# assert registration
		self.assertNotEqual(u,[])

		# assert data is retreived correctly
		u = u[0]
		self.assertEqual(u.username,"n")
		self.assertTrue(check_password_hash(u.password,"n"))		
		self.assertEqual(u.email,"g@g.com")

		# assert register method works only on unregistred users
		self.assertRaises(UserAlreadyRegistredException,u.register)

		# assert no duplicate emails are allowed on registration
		self.assertRaises(EmailAlreadyExistsException,User("n","n","g@g.com").register)

		# assert deletion 
		u.delete()
		self.assertEqual(User.query({"email":"g@g.com"}),[])

	def test_update(self):

		u = User("a","a","a@g.com")

		newData = {"email":"ff@ff.com"}

		# assert update only works on registred users
		f = lambda : u.update(newData)
		self.assertRaises(UserNotRegistredException,f)

		# assert values are updated
		u.register().update(newData)
		for key,v in newData.items():
			self.assertEqual(getattr(u,key),v)

		# assert no duplicate emails are allowed on update
		u = User("a","a","f@f.com").register()
		f = lambda : u.update(newData)
		self .assertRaises(EmailAlreadyExistsException,f)
