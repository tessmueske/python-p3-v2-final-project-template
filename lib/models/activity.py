# lib/models/activity.py
from models.__init__ import CURSOR, CONN
from models.destination import Destination #because an activity is owned by a destination, we import Destination into the Activity class