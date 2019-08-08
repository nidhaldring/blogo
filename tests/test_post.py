

import unittest

from models.post import Post
from models.exceptions import *
from tests.commonMockObjects import *


# mock objects
class Author:
	pass

class MockDbManager:
	def execute(self,sql):
		return [("1","1","1","1")]

#

class TestPost(unittest.TestCase):

	def __init__(self,*args,**kargs):
		super().__init__(*args,**kargs)
		Post.dbManager = MockDbManager()
		Post.queryMaker = MockQueryMaker()

	def setUp(self):

		self.author = Author()
		self.post = Post("title","body",self.author)

	def test_insert_raise_when_reinserted(self):

		self.post.insert()
		self.assertRaises(PostAlreadyInsertedException,self.post.insert)

	def test_insert_set_id(self):

		self.post.insert()
		self.assertFalse(self.post.id is None)

	def test_delete_raises_when_deleting_non_inserted_posts(self):

		self.assertRaises(PostNotInsertedException,self.post.delete)

	def test_delete_set_id_to_None(self):

		self.post.insert()
		self.post.delete()
		self.assertEqual(self.post.id,None)


	def test_update_changes_object_values_inplace(self):

		self.post.insert()
		self.post.update({"body":"ttt"})
		self.assertEqual(self.post.body,"ttt")

	def test_update_raises_when_updating_uninserted_posts(self):

		self.assertRaises(PostNotInsertedException,self.post.update,{"body":"5"})

	def test_query_returns_list_of_post_objects_with_correct_query_condition(self):

		posts = Post.query({"title":"1"})
		self.assertNotEqual(posts,[])
		self.assertEqual(posts[0].title,"1")


