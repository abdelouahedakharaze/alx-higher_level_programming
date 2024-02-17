#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Constructs the URI for database connection
    db_uri = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )

    # Creates an engine with pre-ping enabled
    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creates a session and binds it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieves all State objects along with their associated City objects
    states = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    # Prints each State object along with its corresponding City objects
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
