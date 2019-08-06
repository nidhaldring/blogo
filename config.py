
import os


class Config:

	TESTING = False
	SECRET_KEY = os.urandom(10)
	DB_NAME = "blog"
	USERS_TABLE = "root"
	DB_PASSWORD = "root"
	DB_HOST = "localhost"


class TestingConfig(Config):

	TESTING = True
