
import os


class Config:

	TESTING = False
	SECRET_KEY = os.urandom(10)

	ENGINE_URI = "mysql+pymysql://localhost/tests"
	USERS_TABLE = "users"
	POSTS_TABLE = "posts"

	UPLOAD_FOLDER = "uploads"
	DEFAULT_USER_PIC_LOCATIONS = "uploads/profile.png"
	ALLOWED_EXTENSIONS = {"png","jpg","jpeg"}
