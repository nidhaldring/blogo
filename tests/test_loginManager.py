
'''
import unittest

from utils.loginManager import loginUser,logoutUser
from models.user import User
from createApp import createApp
from config import TestingConfig


class TestLoginManager(unittest.TestCase):

	def __init__(self):

		User.DB = dict(db="test",user="root",password="root",host="localhost")
		self.user = User("nidhal","fff","ff@fff.com")

	def test_loginUser_logoutUser(self):

		app = createApp(TestingConfig)
		with app.test_client() as client:

			loginUser(self.user)
'''

