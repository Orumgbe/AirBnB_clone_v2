#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import models
from os import getenv
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


class empty_class:
    """Does nothing"""
    pass


storage_type = getenv('HBNB_STORAGE_USER')
if storage_type == "db":
    Base = declarative_base()
else:
    Base = empty_class()


class BaseModel:
    """A base class for all hbnb models"""
    if storage_type == "db"
        id = Column(String(60), primary_key=True, nullable=False, unique=True)
        created_at = Column(DateTime(), default=datetime.utcnow())
        updated_at = Column(DateTime(), default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            try:
                del kwargs['__class__']
            except KeyError:
                pass
            for key, value in kwargs.items():
                if key == 'updated_at':
                    kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                             '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    setattr(self, key, value)
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes current instance from storage"""
        models.storage.delete(self)
