from sqlalchemy import Column, Integer, String, Float, Text
from .database import Base

class PointData(Base):
    __tablename__ = 'points'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

class PolygonData(Base):
    __tablename__ = 'polygons'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    coordinates = Column(Text, nullable=False)  # Store as JSON string
