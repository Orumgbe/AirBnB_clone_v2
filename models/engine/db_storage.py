#!/usr/bin/python3
"""Handles database storage using mysql"""

from os import getenv
from models.base_model import Base
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Database storage engine"""
    __engine = None
    __session = None

    cls_dict = {"User": User, "Place": Place, "State": State, "City": City,
                "Review": Review, "Amenity": Amenity}

    def __init__(self):
        """Instantiates DBStorage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
                                             HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects on database or cls instance only if specified"""
        all_obj = {}
        if cls is None:
            for c_name in self.cls_dict.values():
                c_obj = self.__session.query(c_name).all()
                for obj in c_obj:
                    key = c_name + '.' + str(obj.id)
                    all_obj.update({key: obj})
        else:
            for obj in self.__session.query(cls).all():
                key = cls + '.' + str(obj.id)
                all_obj.update({key: obj})
        return all_obj

    def new(self, obj):
        """Adds new object to database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes only specified obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session_thread = scoped_session(Session)
        self.__session = session_thread()
