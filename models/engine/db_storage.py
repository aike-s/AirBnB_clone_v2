#!/usr/bin/python3
"""File of DBStorage class"""
from sqlalchemy import create_engine
from os import getenv
from base_model import Base
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
        """Return """