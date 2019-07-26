

import unittest

import pymysql

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
		u = User.query({"email":"g@g.com"})[0]

		self.assertNotEqual(u,[])
		self.assertEqual(u.username,"n")
		self.assertEqual(u.password,"n")
		self.assertEqual(u.email,"g@g.com")

		u.delete()
		self.assertEqual(User.query(dict(email="x")),[])




