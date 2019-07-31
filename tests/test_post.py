

import unittest

import pymysql

from models.post import Post
from models.user import User
from models.exceptions import *


Post.DB_CON = dict(host="localhost",db="test",user="root",password="root")

class TestPost(unittest.TestCase):


	def setUp(self):

		self.author = User("f","f","f@f.com").register()
		self.post = Post("title","body",self.author.id)

	def tearDown(self):

		conn = pymysql.connect(**Post.DB_CON)
		cursor = conn.cursor()
		cursor.execute("delete from posts;")
		cursor.execute("delete from users;")
		conn.commit()
		conn.close()


	def test_insert_update_db(self):
		
		self.post.insert()
		posts = Post.query({"id":self.post.id})
		self.assertTrue(len(posts) == 1)

		post = posts[0]
		self.assertEqual(post.body,self.post.body)
		self.assertEqual(post.title,self.post.title)
		self.assertEqual(post.id,self.post.id)

	def test_insert_raise_when_reinserted(self):

		self.post.insert()
		self.assertRaises(PostAlreadyInsertedException,self.post.insert)

	def test_insert_set_id(self):

		self.post.insert()
		self.assertFalse(self.post.id is None)

	def test_delete_update_db(self):

		self.post.insert()
		self.post.delete()
		self.assertEqual(Post.query({"id":self.post.id}),[])

	def test_delete_raises_when_deleting_non_inserted_posts(self):

		self.assertRaises(PostNotInsertedException,self.post.delete)

	def test_delete_set_id_to_None(self):

		self.post.insert()
		self.post.delete()
		self.assertEqual(self.post.id,None)


	def test_update_changes_values(self):

		self.post.insert()
		self.post.update({"body":"ttt"})
		self.assertEqual(self.post.body,"ttt")

	def test_update_update_db(self):

		self.post.insert()
		self.post.update({"body":"ttt"})
		post = Post.query({"id":self.post.id})[0]

		self.assertEqual(post.body,"ttt")

	def test_update_raises_when_updating_uninserted_posts(self):

		self.assertRaises(PostNotInsertedException,self.post.update,{"body":"5"})


