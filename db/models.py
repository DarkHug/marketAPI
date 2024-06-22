from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Boolean, ForeignKey, Column, Text
from db.config import Base


class Sellers(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Используйте String для хранения email
    password = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)


class Types(Base):
    __tablename__ = 'types'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class VPavilions(Base):
    __tablename__ = 'vegetable_pavilion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price_per_kg = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    seller_id = Column(Integer, ForeignKey('sellers.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)


class MPavilions(Base):
    __tablename__ = 'market_pavilion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    at_discount = Column(Boolean, default=False)
    discount_price = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    seller_id = Column(Integer, ForeignKey('sellers.id'), nullable=False)
