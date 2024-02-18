#!/usr/bin/python3
"""
Defines a class to
manage file  storage
for hbnb clone
"""
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

class DBStorage:
    """
    class
    DBStorage
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        init function
        """
        db_user = getenv("HBNB_MYSQL_USER")
        db_pass = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_db = getenv("HBNB_MYSQL_DB")
        db_env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{db_user}:{db_pass}@{db_host}/{db_db}",
            pool_pre_ping=True,
        )

        if db_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """
        Method to reload
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = Session()

    def all(self, cls=None, id=None):
        """
        A querry for all
        classes
        """
        classes = [User, Place, State, City, Amenity, Review]
        res = {}

        if cls is not None:
            if id is not None:
                ob = self.__session.query(cls).get(id)
                if ob is not None:
                    Name_of_class = ob.__class__.__name__
                    kyName = Name_of_class + "." + str(ob.id)
                    res[kyName] = ob
            else:
                for ob in self.__session.query(cls).all():
                    Name_of_class = ob.__class__.__name__
                    kyName = Name_of_class + "." + str(ob.id)
                    res[kyName] = ob
        else:
            for css in classes:
                if id is not None:
                    ob = self.__session.query(css).get(id)
                    if ob is not None:
                        Name_of_class = ob.__class__.__name__
                        kyName = Name_of_class + "." + str(ob.id)
                        res[kyName] = ob
                else:
                    for ob in self.__session.query(css).all():
                        Name_of_class = ob.__class__.__name__
                        kyName = Name_of_class + "." + str(ob.id)
                        res[kyName] = ob
        return res

    def search(self, cls, id):
        """
        """
        data = self.all(cls)

    def new(self, obj):
        """
        Adds New object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Used to save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Removes from database
        """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """
        close session
        """
        self.__session.close()
