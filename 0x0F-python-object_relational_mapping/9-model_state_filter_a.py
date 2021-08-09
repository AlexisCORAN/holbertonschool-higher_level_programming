#!/usr/bin/python3
"""
THis script lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    content = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(content.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    c = '%a%'
    states = session.query(State).filter(State.name.like(c)).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
