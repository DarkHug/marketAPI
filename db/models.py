from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey, Column
from config import Base


class Sellers(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
