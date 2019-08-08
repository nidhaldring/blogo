
import os


class Config:

	TESTING = False
	SECRET_KEY = os.urandom(10)
	DB_NAME = "blog"
	DB_PASSWORD = "root"
	DB_HOST = "localhost"
	USERS_TABLE = "users"
	POSTS_TABLE = "posts"


class TestingConfig(Config):

	TESTING = True
