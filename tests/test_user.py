

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




