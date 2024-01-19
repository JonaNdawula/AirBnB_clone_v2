#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage
from models.user import User
from models.state import State

Store_type = getenv('HBNB_TYPE_STORAGE')

if Store_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
