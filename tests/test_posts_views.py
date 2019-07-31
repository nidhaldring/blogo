

import unittest

from createApp import createApp
from config import TestingConfig
from models.post import Post
from models.user import User


class TestPostsViews(unittest.TestCase):

	def __init__(self,*args,**kargs):

		super().__init__(*args,**kargs)
		self.app = createApp(TestingConfig)


	def test_posts_view_return_200_when_acessing_posts(self):

		with self.app.test_client() as client:

			author = User("n","f","f@f.com").register()
			post = Post("ggg","fff",author.id).insert()
			resp = client.get(f"/posts/{post.id}",follow_redirects=True)
		
			post.delete()
			author.delete()

			self.assertEqual(resp.status_code,200)


	def test_posts_view_return_404_when_post_not_exists(self):

		with self.app.test_client() as client:
			resp = client.get("/posts/0",follow_redirects=True)
			self.assertEqual(resp.status_code,404)