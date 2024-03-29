#!/usr/bin/python3
"""
This script retrieves all State objects
from the database named `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and retrieve the states.
    """

    db_uri_template = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    db_uri = db_uri_template.format(argv[1], argv[2], argv[3])

    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    for instance in session.query(State).order_by(State.id):
        print("{0}: {1}".format(instance.id, instance.name))
