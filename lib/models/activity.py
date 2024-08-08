# lib/models/activity.py
from models.__init__ import CURSOR, CONN
from models.destination import Destination #because an activity is owned by a destination, we import Destination into the Activity class. 

class Activity:
    
    all = {}

    def __init__(self, name, price, length_of_time, plan_ahead, destination_name):
        self.name = name
        self.price = price
        self.length_of_time = length_of_time
        self.plan_ahead = plan_ahead
        self.destination_name = destination_name
        
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
            raise Exception("Response must be either True (for yes) or False (for no)")
        return self._plan_ahead

    @property
    def destination_name(self):
        return self._destination_name

    @destination_name.setter
    def destination_name(self, value):
        if not isinstance(value, str):
            raise Exception("Destination name must be only letters of the alphabet")
        return self._destination_name

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Activity instances """
        sql = """
            CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price FLOAT,
            length_of_time INTEGER,
            plan_ahead BOOLEAN,
            destination_name TEXT,
            FOREIGN KEY (destination_name) REFERENCES destinations(name))
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
        """ Insert a new row with the name, job title, and destination name values of the current Activity object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO activities (name, price, length_of_time, plan_ahead, destination_name)
                VALUES (?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.price, self.length_of_time, self.plan_ahead, self.destination_name))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Activity instance."""
        sql = """
            UPDATE activities
            SET name = ?, price = ?, length_of_time = ? plan_ahead = ?, destination_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.price, self.length_of_time, self.plan_ahead, self.destination_name, self.id))
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

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, price, length_of_time, plan_ahead, destination_name):
        """ Initialize a new Activity instance and save the object to the database """
        activity = cls(name, price, length_of_time, plan_ahead, destination_name)
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
        else:
            # not in dictionary, create new instance and add to dictionary
            activity = cls(row[1], row[2], row[3], row[4])
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
    def find_by_name(cls, name):
        """Return Activity object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM activities
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_price(cls, price):
        """Return Activity object corresponding to first table row matching specified price"""
        sql = """
            SELECT *
            FROM activities
            WHERE price is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_length_of_time(cls, length_of_time):
        """Return Activity object corresponding to first table row matching specified length_of_time"""
        sql = """
            SELECT *
            FROM activities
            WHERE length_of_time is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


#Activities:

# Córdoba - 
    # 1. 
        # Name: Mezquita Cathedral de Cordoba
        # Price:
        # Length of time:
        # Planned ahead?
    # 2. Alcazar de los Reyes Cristianos
        # Price:
        # Length of time:
        # Planned ahead?

# Alicante - 
    # 1. 
        # Name: Mercat Central d'Alacant
        # Price:
        # Length of time:
        # Planned ahead?
    # 2. 
        # Name: Guadalest Valley
        # Price:
        # Length of time:
        # Planned ahead?

# Barcelona - 
    # 1.
        # Name: Parc Güell
        # Price:
        # Length of time:
        # Planned ahead? 
    # 2. 
        # Name: Ciutat Vella (Old City)
        # Price: $0.00
        # Length of time: 1
        # Planned ahead? False
    # 3.
        # Name: Barri Gòtic (Gothic Quarter)
        # Price: $0.00
        # Length of time: 1
        # Planned ahead? False
    # 4.
        # Name: La Sagrada Família
        # Price:
        # Length of time:
        # Planned ahead? True
    # 5.
        # Name: Candy Darling (queer bar)
        # Price:
        # Length of time: 2
        # Planned ahead? False
    # 6. 
        # Name: Antoni Gaudí walking tour
        # Price:
        # Length of time:
        # Planned ahead? 

# Granada - 
    # 1.
        # Name: La Alhambra
        # Price:
        # Length of time:
        # Planned ahead? True
    # 2.
        # Name: Albaicín (neighborhood)
        # Price: $0.00
        # Length of time:
        # Planned ahead? False
    # 3.
        # Name: Mirador de San Cristóbal
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Catedral de Granada
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: Buy Moroccan and Turkish decor
        # Price:
        # Length of time: 1
        # Planned ahead? False

# Madrid - 
    # 1.
        # Name: Fun Fun wine bar
        # Price: $10.00
        # Length of time: 1
        # Planned ahead? False
    # 2.
        # Name: Sala Equis (old cinema turned bar)
        # Price: $10.00
        # Length of time: 2
        # Planned ahead? False
    # 3.
        # Name: El Prado Museum
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Reina Sofía Museum
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: Fulanita de Tal (lesbian bar)
        # Price: $0.00
        # Length of time: 3
        # Planned ahead? False
    # 6.
        # Name: Almudena Cathedral
        # Price:
        # Length of time:
        # Planned ahead?
    # 7.
        # Name: Templo de Debod
        # Price: $0.00
        # Length of time: 1
        # Planned ahead? False
    # 8.
        # Name: El Retiro Park
        # Price: $0.00
        # Length of time: 2
        # Planned ahead? False

# Valencia - 
    # 1. 
        # Name: Eat paella
        # Price: $30.00
        # Length of time: 2
        # Planned ahead? False
    # 2.
        # Name: Mercat Central de Valencia
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: La Lonja de la Seda
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Valencia Cathedral
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: Plaza de la Virgen
        # Price:
        # Length of time:
        # Planned ahead?
    # 6.
        # Name: Casco Historico
        # Price:
        # Length of time:
        # Planned ahead?

# Seville - 
    # 1.
        # Name: Drink orange wine
        # Price:
        # Length of time:
        # Planned ahead?
    # 2.
        # Name: Eat oranges
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: Plaza de España
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Maria Luisa Park
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: Royal Alcázar
        # Price:
        # Length of time:
        # Planned ahead?
    # 6.
        # Name: Seville Cathedral
        # Price:
        # Length of time:
        # Planned ahead?
    # 7.
        # Name: Watch Flameno dancers
        # Price:
        # Length of time:
        # Planned ahead?

# Bilbao - 
    # 1.
        # Name: Iralabarri neighborhood
        # Price:
        # Length of time:
        # Planned ahead?
    # 2. 
        # Name: a Sinsorga (feminist restaurant)
        # Price:
        # Length of time:
        # Planned ahead?
    # 3. 
        # Name: Espacio Open (cultural center)
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: visit Elantxobe (tiny fishing village with one street)
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: Nervión River
        # Price:
        # Length of time:
        # Planned ahead?
    # 6.
        # Name: Casco Viejo (old neighborhood)
        # Price:
        # Length of time:
        # Planned ahead?

# Toledo - 
    # 1.
        # Name: Puente San Martin over the Tagus River
        # Price:
        # Length of time:
        # Planned ahead?
    # 2. 
        # Name: Santa Iglesia Catedral Primada de Toledo
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: Toledo Historic Center
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Monastery of San Juan de los Reyes
        # Price:
        # Length of time:
        # Planned ahead?

# Zaragoza - 
    # 1.
        # Name: El Tubo (neighborhood)
        # Price:
        # Length of time:
        # Planned ahead?
    # 2. 
        # Name: El Ebro River
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: La Seo del Salvador
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: Basilica de Nuestra Senora del Pilar
        # Price:
        # Length of time:
        # Planned ahead?
    # 5. 
        # Name: Palacio de la Aljafería
        # Price:
        # Length of time:
        # Planned ahead?

# Rioja - 
    # 1.
        # Name: wine tasing
        # Price: $30.00
        # Length of time: 2
        # Planned ahead? False
    # 2.
        # Name: Castle of Clavijo
        # Price:
        # Length of time:
        # Planned ahead?

# Balearic Islands - 
    # 1.
        # Name: surfing
        # Price:
        # Length of time:
        # Planned ahead?
    # 2.
        # Name: explore the beaches
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: swimming in the sea
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: tan on the beach
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: party in Ibiza
        # Price: $100.00
        # Length of time: 8
        # Planned ahead? False

# Canary Islands - 
    # 1.
        # Name: visit for Carnaval
        # Price:
        # Length of time:
        # Planned ahead?
    # 2.
        # Name: Parque Nacional de Teide
        # Price:
        # Length of time:
        # Planned ahead?
    # 3.
        # Name: stargazing
        # Price: $0.00
        # Length of time: 1
        # Planned ahead? False
        # Name: sailing
        # Price:
        # Length of time:
        # Planned ahead?
    # 4.
        # Name: La Tejita (nude beach)
        # Price:
        # Length of time:
        # Planned ahead?
    # 5.
        # Name: try almogrote
        # Price:
        # Length of time:
        # Planned ahead?
    # 6.
        # Name: take a boat to Playa de Antequera
        # Price:
        # Length of time:
        # Planned ahead?
    # 7.
        # Name: Mercadillo del Agricultor de Tacoronte (little local market)
        # Price:
        # Length of time:
        # Planned ahead?
    # 8.
        # Name: Lanzarote
        # Price:
        # Length of time:
        # Planned ahead?