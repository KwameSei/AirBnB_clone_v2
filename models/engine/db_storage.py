#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        user = os.environ.get("HBNB_MYSQL_USER")
        password = os.environ.get("HBNB_MYSQL_PWD")
        host = os.environ.get("HBNB_MYSQL_HOST")    # (here = localhost)
        database = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                                user,
                                                password,
                                                host,
                                                database,
                                                pool_pre_ping=True))

        if (env == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
            query on the current database session (self.__session)
            all objects depending of the class name (argument cls)
        """
        """
            all_classes = ["State", "City", "Amenity",
            "User", "Place", "Review"]

            entities = dict()

            if cls:
                return self.get_data_from_table(cls, entities)

            for entity in all_classes:
                entities = self.get_data_from_table(eval(entity), entities)
            return entities
        """
        """ Queries a database for objects """
        """
        if not cls:
            from models.state import State
            from models.city import City

            res_list = (self.__session.query(State)).all()
            res_list.extend(self.__session.query(User))
            #res_list.extend(self.__session.query(Amenity))
            res_list.extend(self.__session.query(City))
            res_list.extend(self.__session.query(Place))
            res_list.extend(self.__session.query(Review))
           # res_list.extend(self.__session.query(City))
        else:
            res_list = self.__session.query(cls).all()

        if res_list:
            return {'{}.{}'.format(type(obj).__name__, obj.id): obj
                for obj in res_list}
        else:
         print("Welcome")
        """

        obj_dict = {}

        if cls is None:
            classes = {'State': State, 'City': City, 'User': User,
                       'Place': Place, 'Review': Review, 'Amenity': Amenity}

            for key, value in classes.items():
                all_obj = self.__session.query(value).all()

                for one_obj in all_obj:
                    key = "{}.{}".format(type(one_obj).__name__, one_obj.id)
                    # Print (key)
                    obj_dict[key] = one_obj
        else:
            if type(cls) == str:
                cls = eval(cls)
                all_obj = self.__session.query(cls)
                for one_obj in all_obj:
                    key = one_obj.__class__.__name__ + '.' + one_obj.id
                    #key = "{}.{}".format(type(one_obj).__name__,
                    #                    one_obj.id)
                    obj_dict[key] = one_obj

         #       print(obj_dict)
        return obj_dict

    def new(self, one_obj):
        """Adds new object to the current database session"""
        self.__session.add(one_obj)

    def save(self):
        """Commit all changes to the current database"""
        self.__session.commit()

    def reload(self):
        """Creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def delete(self, one_obj=None):
        """Deletes from the current database"""
        if (one_obj):
            self.__session.delete(one_obj)
        else:
            pass

    def close(self):
        """Closing the session"""
        self.__session.close()
