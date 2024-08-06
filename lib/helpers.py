# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

def exit_():
    print("thanks for planning! happy travels :)")
    exit()

def create_destination():
    print("creating destination...")

def list_all_destinations_by_name():
    print("listing all destinations...")
    #for i, destination in enumerate(destinations, start = 1):
    #    print(f”{i}.  {destination.name}”)

def find_destination_by_name():
    print("finding destination...")

def update_destination():
    print("updating destination...")

def delete_destination():
    print("deleting destination...")

def create_activity():
    print("creating activity...")

def list_all_activities_by_name():
    print("listing all activities...")
    #for i, activity in enumerate(activities, start = 1):
    #    print(f”{i}.  {activity.name}”)

def find_activity_by_name():
    print("finding activity...")

def update_activity():
    print("updating activity...")

def delete_activity():
    print("deleting activity...")

# A handy dandy tip is using enumerate to iterate with an index in python!
# for i, value in enumerate(values, start=1):
#     		print(i, value)

# For my dogs I can use get_all to get a list of dog objects.  To print them out nicely numbered I can do:
# for i, dog in enumerate(dogs, start=1):
#     		print(f”{i}.  {dog.name}”)

# Now the dogs are printed out with sequential numbers (not their id’s) and the client can select one using that number.

# Since I got the dogs from the backend using .get_all() and iterated through the list as shown above, if the user wants number 3, I know the user wants the third one in that list and I can just grab it from dogs - but the 3rd dog's index in the list is 2 (because the first item in a list is at index 0).  dogs is a list of dog objects, so if the user says "I pick 3" I show them dogs[number_they_picked - 1] and voila!  I have the dog (an object) they wanted with all its attributes available to me to show them!! 