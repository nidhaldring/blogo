
from werkzeug.security import generate_password_hash
from sqlalchemy import *
from sqlalchemy.orm import relationship

from config import Config
from models.model import ModelMixin,Base

class User(Base,ModelMixin):
	__tablename__ = Config.USERS_TABLE
	_id = Column(Integer,primary_key=True)
	username = Column(String(64),nullable=False)
	_password = Column(String(96),nullable=False)
	email = Column(String(96),nullable=False,unique=True)
	pic = Column(String(96),default="profile.png")
	posts = relationship("Post",back_populates="user")

	def __init__(self,*,username,password,email):
		self.username = username
		self.password = password
		self.email = email

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self,p:str):
		self._password = generate_password_hash(p)
