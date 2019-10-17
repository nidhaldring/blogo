
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from config import Config

eng = create_engine(Config.ENGINE_URI)
Base = declarative_base(bind=eng)

class ModelMixin:

	session = Session(bind=eng)

	def insert(self):
		try:
			self.session.add(self)
			self.session.commit()
		except Exception as e:
			self.session.rollback()
			raise e

	def delete(self):
		try:
			self.session.delete(self)
			self.session.commit()
		except Exception as e:
			self.session.rollback()
			raise e

	@classmethod
	def query(cls):
		return cls.session.query(cls)
