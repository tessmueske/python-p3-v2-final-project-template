# lib/models/activity.py
from models.__init__ import CURSOR, CONN
from models.destination import Destination #because an activity is owned by a destination, we import Destination into the Activity class. 

class Activity:

    all = {}
    
    def __init__(self, name, price, length_of_time, plan_ahead, destination_id, id = None):
        self.id = id
        self.name = name
        self.price = price
        self.length_of_time = length_of_time
        self.plan_ahead = plan_ahead
        self.destination_id = destination_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("activity name must only have letters.")
        if len(value) <= 0:
            raise Exception("activity name must be greater than zero characters.")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise Exception("activity price must be look like this: $0.00")
        self._price = value

    @property
    def length_of_time(self):
        return self._length_of_time

    @length_of_time.setter
    def length_of_time(self, value):
        if not isinstance(value, int):
            raise Exception("activity's time length must be a whole number represented in hours (ie 2)")
        self._length_of_time = value
    
    @property
    def plan_ahead(self, value):
        if isinstance(value, bool):
            self._plan_ahead = value
        elif value in ["yes", "true"]:
            self._plan_ahead = True
        elif value in ["no", "false"]:
            self._plan_ahead = False
        else:
            raise Exception('response must be either "yes", "true", "no", or "false"')

    @property
    def destination_id(self):
        return self._destination_id

    @destination_id.setter
    def destination_id(self, destination_id):
        if type(destination_id) is int and Destination.find_by_id(destination_id):
            self._destination_id = destination_id
        else:
            raise ValueError(
                "destination_id must reference a destination in the database")

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of Activity instances"""
        sql = """
        CREATE TABLE IF NOT EXISTS activities (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price FLOAT,
        length_of_time INTEGER,
        plan_ahead BOOLEAN,
        destination_id INTEGER,
        FOREIGN KEY (destination_id) REFERENCES destinations(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit() 

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Activity instances """
        sql = """
            DROP TABLE IF EXISTS activities;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, price, length of time, plan ahead, and destination id values of the current Activity object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO activities (name, price, length_of_time, plan_ahead, destination_id)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, float(self.price), int(self.length_of_time), bool(self.plan_ahead), self.destination_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Activity instance."""
        sql = """
            UPDATE activities
            SET name = ?, price = ?, length_of_time = ?, plan_ ahead = ?, destination_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.length_of_time, self.plan_ahead,
                             self.destination_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Activity instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM activities
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, price, length_of_time, plan_ahead, destination_id):
        """ Initialize a new Activity instance and save the object to the database """
        activity = cls(name, float(price), int(length_of_time), bool(plan_ahead), destination_id)
        activity.save()
        return activity

    @classmethod
    def instance_from_db(cls, row):
        """Return an Activity object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        activity = cls.all.get(row[0])
        if activity:
            # ensure attributes match row values in case local instance was modified
            activity.name = row[1]
            activity.price = row[2]
            activity.length_of_time = row[3]
            activity.plan_ahead = row[4]
            activity.destination_id = row[5]
        else:
            # not in dictionary, create new instance and add to dictionary
            activity = cls(row[1], row[2], row[3], row[4], row[5])
            activity.id = row[0]
            cls.all[activity.id] = activity
        return activity

    @classmethod
    def get_all(cls):
        """Return a list containing one Activity object per table row"""
        sql = """
            SELECT *
            FROM activities
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Activity object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM activities
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Activity object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM activities
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None