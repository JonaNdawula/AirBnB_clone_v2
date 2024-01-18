#!/usr/bin/python3
"""
Defines a class to
manage file  storage
for hbnb clone
"""
from models.base_model import Base
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


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
            pool_pre_ping=True
        )

        if db_env == "test":
            Base.metadata.drop_all(self.engine)

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
                    name_of_class = ob.__class__.__name__
                    kyName = name_of_class + "." + str(ob.id)
                    res[kyName] = ob
            else:
                for ob in self.session.query(cls).all():
                    name_of_class = ob.__class__.__name__
                    kyName = name_of_class + "." + str(ob.id)
                    res[kyName] = ob
        else:
            for css in classes:
                if id is not None:
                    ob = self.__session.query(css).get(id)
                    if ob is not None:
                        name_of_class = ob.__class__.__name__
                        kyName = name_of_class + "." + str(ob.id)
                        res[kyName] = ob
                    else:
                        for ob in self.session.query(css).all():
                            name_of_class = ob.__class__.__name__
                            kyName = name_of_class + "." + str(ob.id)
                            res[kyName] = ob
        return res

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.session = Session()

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
        self.session.close()
