#!/usr/bin/python3
'''Contains the description of the 'City' model representing a city's
information on the database
'''

from sqlalchemy import Integer
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import ForeignKey
from relationship_state import Base, State


class City(Base):
    ''''City' Model -> Represents a city's information on the database.
    '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
