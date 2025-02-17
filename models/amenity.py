#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

store_type = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """ document doc"""
    __tablename__ = 'amenities'
    if store_type == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary='place_amenity',
            back_populates="amenities")
    else:
        name = ""
