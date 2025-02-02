#!/usr/bin/python3
"""
Initializes an instance of the data storage class.
"""
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
