#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")

    else:
        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            cities_list = []
            all_cities = models.storage.all(City)

            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
