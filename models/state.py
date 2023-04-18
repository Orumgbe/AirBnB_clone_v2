#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __table_name = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            city.list = []
            for city in storage.all(City).value():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
