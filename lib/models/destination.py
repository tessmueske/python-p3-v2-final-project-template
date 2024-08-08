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
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Destination instances """
        sql = """
            CREATE TABLE IF NOT EXISTS destinations (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT)
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
        """ Insert a new row with the name and location values of the current Destination instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO destination (name)
            VALUE (?)
        """

        CURSOR.execute(sql, (self.name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Destination instance and save the object to the database """
        destination = cls(name)
        destination.save()
        return destination

    def update(self):
        """Update the table row corresponding to the current Destination instance."""
        sql = """
            UPDATE destination
            SET name = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Destination instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM destination
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def get_all(cls):
        """Return a list containing a Destination object per row in the table"""
        sql = """
            SELECT *
            FROM destination
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        """Return a Destination object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM destination
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def activities(self):
        """Return list of activities associated with current destination"""
        from models.activity import Activity
        sql = """
            SELECT * FROM activity
            WHERE destination_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

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