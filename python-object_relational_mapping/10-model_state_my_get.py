#!/usr/bin/python3
'''List all States'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    name = sys.argv[4]
    first = session.query(State).filter(State.name.contains(name)).first()

    if first:
        print("{}".format(first.id))
    else:
        print('Not found')

    session.close()
