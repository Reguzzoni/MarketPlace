from datetime import datetime

from sqlalchemy import select

from entity.marketDataModel import MarketDataEntity
from utils.DBUtils import get_session_from_db

file_name = "crud.py"


def log(log_value, method_name): (
    print(datetime.now(), " - ", file_name, " : ", method_name, " - ", log_value)
)


def insert_market_data():
    method_name = "insert_market_data"

    # Connect to database and schema
    session = get_session_from_db()
    log("Connected to DB and got session", method_name)

    # create rows to insert into DB
    market_data_to_save = []
    market_data_value = 1

    while market_data_value <= 100:
        market_data_entity = MarketDataEntity(
            value=market_data_value,
        )
        market_data_value += 1
        market_data_to_save.append(market_data_entity)

    # insert rows (by bulk collection) into the session
    session.bulk_save_objects(market_data_to_save)
    # commit the transaction to the DB
    session.commit()
    log("Committed to DB", method_name)

    # close session
    session.close()
    log("Closed session", method_name)


def select_all_market_data():
    method_name = "select_all_market_data"

    # Connect to database and schema
    session = get_session_from_db()
    log("Connected to DB and got session", method_name)

    # get all market_data ordered by id
    result = session.execute(select(MarketDataEntity).order_by(MarketDataEntity.mkt_data_id))
    log("Select results from market_data " + ' '.join(str(v) for v in result.scalars().all()), method_name)

    # close session
    session.close()
    log("Closed session", method_name)


if __name__ == "__main__":
    # test insert
    print("START insert_market_data")
    insert_market_data()
    print("FINISHED insert_market_data")

    print("START select_all_market_data")
    select_all_market_data()
    print("FINISHED select_all_market_data")
