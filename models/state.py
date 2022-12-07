#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='delete', backref='states')

    @property
    def cities(self):
        '''returns the list of City instances with state_id
            equals the current State.id
            FileStorage relationship between State and City
        '''
        from models import storage
        related_cities = []

        cities = storage.all(City).items()  # Getting the entire storage - a dictionary
        for city in cities.values():    # Looping through cities for the city objects
            if city.state_id == self.id:
                related_cities.append(city) # Appending to the cities list
        return related_cities
