

import unittest

from flask import request,session
from createApp import createApp
from config import TestingConfig


index_ = "auth.index"

class TestAuthViews(unittest.TestCase):	

	def __init__(self,*args,**kargs):

		super().__init__(*args,**kargs)

		self.app = createApp(TestingConfig)
		self.userData = dict(username="testu",password="testu",email="testu@test.com")

	def test_a_register_view(self):

		with self.app.test_client() as client:
			
			resp = client.get("/auth/register",follow_redirects=True)
			self.assertEqual(200,resp.status_code)

			resp = client.post("/auth/register",data=self.userData,follow_redirects=True)
			self.assertEqual(200,resp.status_code)
			self.assertEqual(index_,request.endpoint)
			self.assertTrue("_user_id" in session)


	def test_b_logout_view(self):

		with self.app.test_client() as client:

			resp = client.get("/auth/logout",follow_redirects=True)
			self.assertEqual(index_,request.endpoint)
			self.assertEqual(200,resp.status_code)
			self.assertTrue("_user_id" not in session)


	def test_c_login_view(self):

		with self.app.test_client() as client:

			resp = client.get("/auth/login")
			self.assertEqual(resp.status_code,200)

			resp = client.post("/auth/login",data=dict(
					username=self.userData["username"],
					password=self.userData["password"]
				),
				follow_redirects=True
			)
			self.assertEqual(resp.status_code,200)
			self.assertEqual(request.endpoint,index_)
			self.assertTrue("_user_id" in session)

			resp = client.get("/auth/login",follow_redirects=True)
			self.assertTrue(request.endpoint,index_)



