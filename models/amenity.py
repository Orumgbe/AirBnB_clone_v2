#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """
    Amenity class
    back_populates indicates thatthe relationship is bidirectional with the
    amenities attribute in the place class serving as a backref
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenity = relationship("Place", secondary="place_amenity",
                                 back_populates="amenities")
