

import unittest

from flask import request
from createApp import createApp
from config import TestingConfig


index_ = "auth.index"

class TestAuthViews(unittest.TestCase):

	def test_register_view(self):

		app = createApp(TestingConfig)
		with app.test_client() as client:
			
			resp = client.get("/auth/register",follow_redirects=True)
			self.assertEqual(200,resp.status_code)

			resp = client.post("/auth/register",data=dict(
					username="testu",
					password="testu",
					email="testu@test.com"
				),
				follow_redirects=True
			)
			self.assertEqual(200,resp.status_code)
			self.assertEqual(index_,request.endpoint)
			self.assertTrue("_user_id" in session)
			
	'''
	def test_login_lougout_views(self):

		app = createApp(TestingConfig)
		with app.test_client() as client:

			resp = client.get("/auth/login")
			self.assertEqual(resp.status_code,200)

			resp = client.post("/auth/login",data=dict(
					username="nidhal",
					password="123"
				),
				follow_redirects=True
			)
			self.assertEqual(resp.status_code,200)
			self.assertEqual(request.endpoint,index_)
			self.assertTrue("_user_id" in session)

			resp = client.get("auth/logout",follow_redirects=True)
			self.assertEqual(resp.status_code,200)
			self.assertEqual(request.endpoint,index_)
			self.assertFalse("_user_id" in session)
	'''