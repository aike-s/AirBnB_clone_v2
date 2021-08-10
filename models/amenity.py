#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy import Column, String

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Initialization of table/class User """

    __tablename__ = 'users'

    name = Column(String(128), nullable=False)
