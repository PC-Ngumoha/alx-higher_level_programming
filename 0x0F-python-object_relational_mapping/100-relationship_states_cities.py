#!/usr/bin/python3
'''Creates two objects based on their relationship with each other
'''
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(username, password, db_name)
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='California')
    new_city = City(name='San Francisco', state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
