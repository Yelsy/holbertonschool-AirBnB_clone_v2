#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref
from models.city import City
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete-orphan"
        )
else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def cities(self):
            from models.city import City
            new_list_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    new_list_cities.append(city)

            return new_list_cities
