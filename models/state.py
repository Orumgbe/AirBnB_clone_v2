#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_STORAGE_TYPE') == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Initializes state class"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_STORAGE_TYPE') != "db":
        @property
        def cities(self, value):
            """getter for cities with given state id"""
            city_list = []
            cities = models.storage.all(City)
            for city in cities:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
