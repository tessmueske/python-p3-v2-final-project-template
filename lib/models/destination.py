# lib/models/destination.py
from models.__init__ import CURSOR, CONN

class Destination:
    pass
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Destination name must only have letters.")
        if len(value) <= 0:
            raise Exception("Destination name must be greater than zero characters.")
        self._name = value