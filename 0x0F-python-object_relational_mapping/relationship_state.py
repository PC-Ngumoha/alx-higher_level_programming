#!/usr/bin/python3
'''Contains the definition of the 'State' model which is used to represent
information about a specific state on the database
'''
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
# from relationship_city import City

Base = declarative_base()


class State(Base):
    ''''State' Model, modelling the representation of a state on the database.
    '''
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
