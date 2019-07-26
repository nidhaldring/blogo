

import unittest

from flask import request
from createApp import createApp
from config import TestingConfig



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
			self.assertEqual("auth.index",request.endpoint)