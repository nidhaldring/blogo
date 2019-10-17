
from werkzeug.security import generate_password_hash
from sqlalchemy import *

from config import Config
from models.model import ModelMixin,Base

class User(Base,ModelMixin):
	__tablename__ = Config.USERS_TABLE
	id = Column(Integer,primary_key=True)
	username = Column(String(64),nullable=False)
	_password = Column(String(96),nullable=False)

	def __init__(self,*,username,password):
		self.username = username
		self.password = password

	@property
	def password(self):
		raise AttributeError("can't access password !")

	@password.setter
	def password(self,p:str):
		self._password = generate_password_hash(p)
