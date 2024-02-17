#!/usr/bin/python3
"""
This script retrieves all City objects
from the database named `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connects to the database to fetch City objects.
    """

    # Declares the URI template for database connection
    db_uri_template = "mysql+mysqldb://{}:{}@localhost:3306/{}"

    # Formats the URI with provided arguments
    db_uri = db_uri_template.format(argv[1], argv[2], argv[3])

    # Creates an engine and generates metadata
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # Establishes a session
    session = Session()

    # Creates a State object for California
    cal_state = State(name="California")

    # Creates a City object for San Francisco
    sfr_city = City(name="San Francisco")

    # Associates San Francisco with California
    cal_state.cities.append(sfr_city)

    # Adds California to the session
    session.add(cal_state)

    # Commits changes
    session.commit()

    # Closes the session
    session.close()
