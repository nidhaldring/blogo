

import unittest

from createApp import createApp
from config import TestingConfig


class TestPostsViews(unittest.TestCase):

	def setUp(self):
		self.app = createApp(TestingConfig)

	def test_posts_view_return_404_when_post_does_not_exists(self):

		with self.app.test_client() as client:
			resp = client.get("/posts/-1",follow_redirects=True)
			self.assertEqual(resp.status_code,404)

	def test_create_view_return_401_when_accessed_by_unauthorized_user(self):

		with self.app.test_client() as client:
			resp = client.get("/posts/create",follow_redirects=True)
			self.assertEqual(resp.status_code,401) # unauthorized
