# lib/models/destination.py
from models.__init__ import CURSOR, CONN

class Destination:
    
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
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Destination instances """
        sql = """
            CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Destination instances """
        sql = """
            DROP TABLE IF EXISTS destinations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name values of the current Destination instance.
        Update object id attribute using the primary key value of new row."""
        sql = """
            INSERT INTO destinations (name)
            VALUES (?)
        """

        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        # Update the list to include the new instance
        Destination.all = [d for d in Destination.all if d.id != self.id]  # Remove old instance if exists
        Destination.all.append(self)

    @classmethod
    def create(cls, name):
        """ Initialize a new Destination instance and save the object to the database """
        destination = cls(name)
        destination.save()
        return destination

    def update(self):
        """Update the table row corresponding to the current Destination instance."""
        sql = """
            UPDATE destinations
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Destination instance,
        delete the instance from the list, and reassign id attribute"""

        sql = """
            DELETE FROM destinations
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Destination.all = [d for d in Destination.all if d.id != self.id]

        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing all Destination objects"""
        return Destination.all

    @classmethod
    def find_by_id(cls, id):
        """Return a Destination object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM destinations
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

        # For my dogs I can use get_all to get a list of dog objects.  To print them out nicely numbered I can do:
            # for i, dog in enumerate(dogs, start=1):
            #     		print(f”{i}.  {dog.name}”)

        # Now the dogs are printed out with sequential numbers (not their id’s) and the client can select one using that number.

        # Since I got the dogs from the backend using .get_all() and iterated through the list as shown above, if the user wants number 3, I know the user wants the third one in that list and I can just grab it from dogs - but the 3rd dog's index in the list is 2 (because the first item in a list is at index 0).  dogs is a list of dog objects, so if the user says "I pick 3" I show them dogs[number_they_picked - 1] and voila!  I have the dog (an object) they wanted with all its attributes available to me to show them!! 

    @classmethod
    def find_by_name(cls, name):
        """Return a Destination object corresponding to the first table row matching the specified name"""
        sql = """
            SELECT *
            FROM destinations
            WHERE name = ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls(row[1]) if row else None

    def activities(self):
        """Return list of activities associated with the current destination"""
        from models.activity import Activity
        sql = """
            SELECT * FROM activities
            WHERE destination_name = ?
        """
        CURSOR.execute(sql, (self.name,))

        rows = CURSOR.fetchall()
        return [
            Activity.instance_from_db(row) for row in rows
        ]

# Destinations:
# Córdoba
# Alicante
# Barcelona
# Granada
# Madrid
# Valencia
# Seville
# Bilbao
# Toledo
# Zaragoza
# Balearic Islands
# Canary Islands
# Rioja