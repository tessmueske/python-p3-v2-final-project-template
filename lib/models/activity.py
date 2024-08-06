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

#Activities:

# Córdoba - Mezquita Cathedral de Cordoba, Alcazar de los Reyes Cristianos

# Alicante - Mercat Central d'Alacant, Guadalest Valley

# Barcelona - Parc Güell, Ciutat Vella (Old City), Barri Gòtic (Gothic Quarter), La Sagrada Família, Candy Darling (queer bar), Antoni Gaudí walking tour

# Granada - La Alhambra, Albaicín (neighborhood), Mirador de San Cristóbal, Catedral de Granada, buy Moroccan and Turkish decor

# Madrid - Fun Fun wine bar, Sala Equis (old cinema turned bar), El Prado Museum, Reina Sofía Museum, Fulanita de Tal (lesbian bar), Almudena Cathedral, Templo de Debod, El Retiro Park

# Valencia - Eat paella, Mercat Central de Valencia, La Lonja de la Seda, Valencia Cathedral, Plaza de la Virgen, Casco Historico

# Seville - Drink orange wine, eat oranges, Plaza de España (it's in Star Wars), Maria Luisa Park, Royal Alcázar, Seville Cathedral, watch Flameno

# Bilbao - Iralabarri neighborhood, La Sinsorga (feminist restaurant), Espacio Open (cultural center), visit Elantxobe (tiny fishing village with one street), Nervión River, Casco Viejo (old neighborhood)

# Toledo - Puente San Martin over the Tagus River, Santa Iglesia Catedral Primada de Toledo, Toledo Historic Center, Monastery of San Juan de los Reyes

# Zaragoza - El Tubo (neighborhood), El Ebro River, La Seo del Salvador, Basilica de Nuestra Senora del Pilar, Palacio de la Aljafería

# Rioja - wine tasing (Rioja is from here), Castle of Clavijo

# Balearic Islands - surfing, explore the beaches, swimming in the sea, tan on the beach, party in Ibiza

# Canary Islands - visit for Carnaval, Parque Nacional de Teide, stargazing, sailing, island hopping, La Tejita (nude beach), try almogrote, take a boat to Playa de Antequera, Mercadillo del Agricultor de Tacoronte (little local market), Lanzarote