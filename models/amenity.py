#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    # Creating many to many relationship
    place_amenities = relationship("Place", secondary=Place.place_amenity, back_populates="amenities")
