
import os


class Config:

	TESTING = False
	SECRET_KEY = os.urandom(10)
	DB_NAME = "blog"


class TestingConfig:

	TESTING = True
	SECRET_KEY = os.urandom(10)
	DB_NAME ="blog"