from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer

Base = declarative_base()


# Entity mapping 1 at 1 every row of table market_data
class MarketDataEntity(Base):
    __tablename__ = 'market_data'
    mkt_data_id = Column(Integer, primary_key=True)
    value = Column(Integer)

    def __repr__(self):
        return "<MarketDataEntity(value={})>" \
            .format(self.value)
