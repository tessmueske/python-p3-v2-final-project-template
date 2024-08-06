# lib/models/activity.py
from models.__init__ import CURSOR, CONN
from models.destination import Destination #because an activity is owned by a destination, we import Destination into the Activity class

class Activity:
    pass
    def __init__(self, name, price, length_of_time, plan_ahead):
        self.name = name
        self.price = price
        self.length_of_time = length_of_time
        self.plan_ahead = plan_ahead

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Activity name must only have letters.")
        if len(value) <= 0:
            raise Exception("Activity name must be greater than zero characters.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise Exception("Activity price must follow this format: $0.00")
        self._price = value

    @property
    def length_of_time(self):
        return self._length_of_time

    @length_of_time.setter
    def length_of_time(self, value):
        if not isinstance(value, int):
            raise Exception("Activity's time length must be a whole number represented in hours (ie 2)")
        self._length_of_time = value
    
    @property
    def plan_ahead(self):
        return self._plan_ahead

    @plan_ahead.setter
    def plan_ahead(self, value):
        if not isinstance(value, bool):
            raise Exception("Response must be either true (for yes) or false (for no)")
        return self._plan_ahead