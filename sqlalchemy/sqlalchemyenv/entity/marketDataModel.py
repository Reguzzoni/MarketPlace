"""
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
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


# Entity mapping 1 at 1 every row of table market_data
class MarketDataEntity(Base):
    __tablename__='market_data_3'

    Indice=Column(Integer(),primary_key=True)
    Date_Time=Column(String())
    Last=Column(Float())
    Bid=Column(Float())
    Ask=Column(Float())
    Volume=Column(Integer())

    def __repr__(self):
        return '''<MarketDataEntity(Indice='{0}',Date_Time='{1}',Dat_Time='{2}',
        Last='{3}',Bid='{4}',Ask='{5}'>'''.format(self.Indice,self.Date_Time,
                                                  self.Last,self.Bid,self.Ask,self.Volume)
