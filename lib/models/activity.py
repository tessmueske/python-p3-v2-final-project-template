# lib/models/activity.py
from models.__init__ import CURSOR, CONN
from models.destination import Destination #because an activity is owned by a destination, we import Destination into the Activity class. 

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
            raise Exception("Response must be either True (for yes) or False (for no)")
        return self._plan_ahead

    # @classmethod
    # def create_table(cls):
    #     """ Create a new table to persist the attributes of Employee instances """
    #     sql = """
    #         CREATE TABLE IF NOT EXISTS employees (
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         job_title TEXT,
    #         department_id INTEGER,
    #         FOREIGN KEY (department_id) REFERENCES departments(id))
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()

    # @classmethod
    # def drop_table(cls):
    #     """ Drop the table that persists Employee instances """
    #     sql = """
    #         DROP TABLE IF EXISTS employees;
    #     """
    #     CURSOR.execute(sql)
    #     CONN.commit()

    # def save(self):
    #     """ Insert a new row with the name, job title, and department id values of the current Employee object.
    #     Update object id attribute using the primary key value of new row.
    #     Save the object in local dictionary using table row's PK as dictionary key"""
    #     sql = """
    #             INSERT INTO employees (name, job_title, department_id)
    #             VALUES (?, ?, ?)
    #     """

    #     CURSOR.execute(sql, (self.name, self.job_title, self.department_id))
    #     CONN.commit()

    #     self.id = CURSOR.lastrowid
    #     type(self).all[self.id] = self

    # def update(self):
    #     """Update the table row corresponding to the current Employee instance."""
    #     sql = """
    #         UPDATE employees
    #         SET name = ?, job_title = ?, department_id = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.name, self.job_title,
    #                          self.department_id, self.id))
    #     CONN.commit()

    # def delete(self):
    #     """Delete the table row corresponding to the current Employee instance,
    #     delete the dictionary entry, and reassign id attribute"""

    #     sql = """
    #         DELETE FROM employees
    #         WHERE id = ?
    #     """

    #     CURSOR.execute(sql, (self.id,))
    #     CONN.commit()

    #     # Delete the dictionary entry using id as the key
    #     del type(self).all[self.id]

    #     # Set the id to None
    #     self.id = None

    # @classmethod
    # def create(cls, name, job_title, department_id):
    #     """ Initialize a new Employee instance and save the object to the database """
    #     employee = cls(name, job_title, department_id)
    #     employee.save()
    #     return employee

    # @classmethod
    # def instance_from_db(cls, row):
    #     """Return an Employee object having the attribute values from the table row."""

    #     # Check the dictionary for  existing instance using the row's primary key
    #     employee = cls.all.get(row[0])
    #     if employee:
    #         # ensure attributes match row values in case local instance was modified
    #         employee.name = row[1]
    #         employee.job_title = row[2]
    #         employee.department_id = row[3]
    #     else:
    #         # not in dictionary, create new instance and add to dictionary
    #         employee = cls(row[1], row[2], row[3])
    #         employee.id = row[0]
    #         cls.all[employee.id] = employee
    #     return employee

    # @classmethod
    # def get_all(cls):
    #     """Return a list containing one Employee object per table row"""
    #     sql = """
    #         SELECT *
    #         FROM employees
    #     """

    #     rows = CURSOR.execute(sql).fetchall()

    #     return [cls.instance_from_db(row) for row in rows]

    # @classmethod
    # def find_by_id(cls, id):
    #     """Return Employee object corresponding to the table row matching the specified primary key"""
    #     sql = """
    #         SELECT *
    #         FROM employees
    #         WHERE id = ?
    #     """

    #     row = CURSOR.execute(sql, (id,)).fetchone()
    #     return cls.instance_from_db(row) if row else None

    # @classmethod
    # def find_by_name(cls, name):
    #     """Return Employee object corresponding to first table row matching specified name"""
    #     sql = """
    #         SELECT *
    #         FROM employees
    #         WHERE name is ?
    #     """

    #     row = CURSOR.execute(sql, (name,)).fetchone()
    #     return cls.instance_from_db(row) if row else None

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