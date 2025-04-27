from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import json

from . import models, schemas
from .database import SessionLocal, engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/points/")
def create_point(point: schemas.PointCreate, db: Session = Depends(get_db)):
    db_point = models.PointData(
        name=point.name,
        latitude=point.lat,
        longitude=point.lon
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return {"id": db_point.id, "message": "Point created successfully"}

@app.post("/polygons/")
def create_polygon(poly: schemas.PolygonCreate, db: Session = Depends(get_db)):
    db_polygon = models.PolygonData(
        name=poly.name,
        coordinates=json.dumps(poly.coordinates)
    )
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return {"id": db_polygon.id, "message": "Polygon created successfully"}

@app.get("/points/")
def get_points(db: Session = Depends(get_db)):
    points = db.query(models.PointData).all()
    return [
        {"id": p.id, "name": p.name, "lat": p.latitude, "lon": p.longitude}
        for p in points
    ]

@app.get("/polygons/")
def get_polygons(db: Session = Depends(get_db)):
    polygons = db.query(models.PolygonData).all()
    return [
        {"id": p.id, "name": p.name, "coordinates": json.loads(p.coordinates)}
        for p in polygons
    ]
