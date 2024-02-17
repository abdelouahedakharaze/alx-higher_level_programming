#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
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

    # Creates a session and binds it to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieves all City objects along with their associated State objects
    cities = session.query(City).join(State).order_by(City.id).all()

    # Prints each City object along with its corresponding State name
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
