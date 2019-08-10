

import unittest

from flask import request,session
from createApp import createApp
from config import TestingConfig

from views.auth.utils import *



class TestAuthViews(unittest.TestCase):	

	def setUp(self):

		self.app = createApp(TestingConfig)

	def test_register_view_returns_200_to_get_request(self):

		with self.app.test_client() as client:			
			resp = client.get("/auth/register")
			self.assertEqual(resp.status_code,200)

	def test_login_view_returns_200_to_get_request(self):

		with self.app.test_client() as client:
			resp = client.get("/auth/login")
			self.assertEqual(resp.status_code,200)

	def test_logout_view_returns_200_to_get_request(self):

		with self.app.test_client() as client:
			resp = client.get("/auth/logout",follow_redirects=True)
			self.assertEqual(resp.status_code,200)
