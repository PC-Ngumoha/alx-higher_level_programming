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
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
