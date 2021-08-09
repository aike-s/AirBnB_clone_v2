#!/usr/bin/python3
"""File of DBStorage class"""
from sqlalchemy import create_engine, engine
from os import getenv
from models.base_model import Base, BaseModel

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Class DBStorage that comunicate with MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(user,
                                             password,
                                             host,
                                             database),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects according to their class name"""
        if cls != None:
            data = self.__session(self.classes()[cls])

        else:
            data = self.__session.query(User).all()
            data += self.__session.query(State).all()
            data += self.__session.query(City).all()
            data += self.__session.query(Amenity).all()
            data += self.__session.query(Place).all()
            data += self.__session.query(Review).all()

        objects_dictionary = {}

        for value in objects_dictionary:
            key = "{}.{}".format(type(value).__name__, value.id)
            objects_dictionary[key] = value

        return objects_dictionary

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
