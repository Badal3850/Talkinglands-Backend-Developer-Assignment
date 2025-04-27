from pydantic import BaseModel
from typing import List

class PointCreate(BaseModel):
    name: str
    lat: float
    lon: float

class PolygonCreate(BaseModel):
    name: str
    coordinates: List[List[float]]  # List of [lon, lat] pairs
