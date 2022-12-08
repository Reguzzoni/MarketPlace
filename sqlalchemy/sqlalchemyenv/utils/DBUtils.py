from config.dbconfig import DATABASE_SCHEMA, DATABASE_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session_from_db():
    # Connect to database and schema
    engine = create_engine(
        DATABASE_URI,
        connect_args={'options': '-csearch_path={}'.format(DATABASE_SCHEMA)}
    )

    # create session to the DB with acid property https://it.wikipedia.org/wiki/ACID
    Session = sessionmaker(bind=engine)
    s = Session()
    return s


if __name__ == "__main__":
    get_session_from_db()
