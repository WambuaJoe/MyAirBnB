#!/usr/bin/python3
# BaseModel class
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ create BaseModel class """
    def __init__(self, id, *args, **kwargs):
        self.id = uuid4()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        