#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
from os import getenv

store_type = getenv("HBNB_TYPE_STORAGE")

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
     ),
)


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = "places"
    if store_type == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            viewonly=False,
            back_populates="place_amenities")
        reviews = relationship('Review', cascade="all,delete", backref="place")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def amenities(self):
            """
            gets doc
            """
            from models import storage
            amens = []
            allAmens = storage.all(Amenity)
            for amen in allAmens.values():
                if amen.id in self.amenity_ids:
                    amens.append(amen)
            return amens

        @property
        def reviews(self):
            """
            gets doc
            """
            from models import storage
            list_of_reviews = []
            all_reviews = storage.all(Review)
            for review in all_reviews.values():
                if review.place_id in self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

        @amenities.setter
        def amenities(self, amenity):
            """
            sets amenities
            """
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
