
from sqlalchemy import *
from sqlalchemy.orm import relationship

from config import Config
from models.model import ModelMixin,Base


class Post(Base,ModelMixin):
    __tablename__ = Config.POSTS_TABLE
    _id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String(64),nullable=False)
    body = Column(String(1024),nullable=False)
    userId = Column(Integer,ForeignKey(Config.USERS_TABLE + "._id"),nullable=False)
    user = relationship("User",back_populates="posts")

    def __init__(self,*,title,body,userId):
        Base.__init__(self)
        self.title = title
        self.body = body
        self.userId = userId
