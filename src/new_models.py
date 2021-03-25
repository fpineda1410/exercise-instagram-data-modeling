import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

class Posts(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    user_id = Column( Integer, ForeignKey('user.id'))
    type_ = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    total_likes = Column(Integer, nullable=False)
    total_comments = Column(Integer, nullable=False)

    def to_dict(self):
        return {}

class user_followers(Base):
    __tablename__ = 'user_followers'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('posts.id'))
    type_ = Column(String(250), nullable=False)
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)
    
class user_feeds(Base):
    __tablename__ = 'user_feeds'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

class post_comments (Base):
    __tablename__='post_comments'

    id = Column (Integer, primary_key=True)
    post_id= Column (Integer, ForeignKey('posts.id'))
    user_id=Column (Integer,ForeignKey('user.id'))
    comments= Column (String(250))
    created_at = Column(Integer, nullable=False)
    updated_at = Column(Integer, nullable=False)

class post_likes (Base):
    __tablename__='post_likes'

    id = Column (Integer, primary_key=True)
    post_id= Column(Integer, ForeignKey('posts.id'))
    user_id=Column(Integer,ForeignKey('user.id'))
    created_at = Column(String(250), nullable=False)
    updated_at = Column(String(250), nullable=False)

render_er(Base, 'new_diagram.png')