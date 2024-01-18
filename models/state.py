#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

str_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    if str_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', coscade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """getter document"""
            from models import storage
            citiesList = []
            citiesAll = storage.all(City)
            for city in citiesAll.values():
                if city.state.id == self.id:
                    citiesList.append(city)
            return citiesList
