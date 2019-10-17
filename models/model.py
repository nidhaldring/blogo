
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import Config

eng = create_engine(Config.ENGINE_URI)
Base = declarative_base(bind=eng)

class ModelMixin:

	session = Session(bind=eng)

	def insert(self):
		self.session.add(self)
		self.session.commit()

	def delete(self):
		self.session.delete(self)
		self.session.commit()

	@classmethod
	def query(cls):
		return cls.session.query(cls)
