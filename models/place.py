#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models import storage_type
import os
from sqlalchemy import Column, Integer, Float, String, ForeignKey


if os.getenv("HBNB_TYPE_STORAGE") == "db":
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'), primary_key=True,
                                 nullable=False))

    class Place(BaseModel):
        """ A place to stay """
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey(cities.id), nullable=False)
        user_id = Column(String(60), ForeignKey(users.id), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=False)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=False)
        longitude = Column(Float, nullable=False)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenity_ids = relationship("Amenity", secondary="place_amenity",
                                   viewonly=False)
else:
    from models.amenity import Amenity

    class Place(BaseModel, Base):
        __tablename__ = 'places'
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """property getter"""
            from models import storage
            amenities = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get(Amenity, amenity_id)
                if amenity:
                    amenities.append(amenity)
            return amenities

        @amenities.setter
        def amenities(self, value):
            """property setter"""
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
