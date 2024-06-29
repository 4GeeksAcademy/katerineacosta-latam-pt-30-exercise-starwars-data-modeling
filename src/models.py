import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    subscription_date = Column(Date(), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False )
    hair_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer, nullable=False)
    climate =  Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)

class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship(User)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
