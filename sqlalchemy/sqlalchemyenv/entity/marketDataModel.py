from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


# Entity mapping 1 at 1 every row of table market_data
class MarketDataEntity(Base):
    __tablename__='market_data'

    Index=Column(Integer(),primary_key=True)
    Date_Time=Column(String())
    Last=Column(Float())
    Bid=Column(Float())
    Ask=Column(Float())
    Volume=Column(Integer())
    Candela=Column(Integer())

    def __repr__(self):
        return '''<MarketDataEntity(Index='{0}',Date_Time='{1}',Last='{2}',
        Bid='{3}',Ask='{4}',Volume='{5}',Candela='{6}'>'''.format(self.Index,self.Date_Time,
                                                                  self.Last,self.Bid,self.Ask,self.Volume,self.Candela)


# ---------

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