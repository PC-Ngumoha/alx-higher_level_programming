#!/usr/bin/python3
'''Lists all the cities in the database by their respective states.
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(username, password, db_name)
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj_list = session.query(
            State.name,
            City.id,
            City.name
        ).outerjoin(State).order_by(City.id).all()
    for obj in obj_list:
        print('{}: ({}) {}'.format(obj[0], obj[1], obj[2]))
