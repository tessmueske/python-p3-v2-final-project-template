# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

def exit_(): #completed
    print("thanks for planning! happy travels :)")
    exit()

def create_destination():
    name = input("Enter the destination's name: ")
    try:
        destination = Destination.create(name)
        print(f'Success: {destination}')
    except Exception as exc:
        print("Error creating destination: ", exc)

def list_all_destinations_by_name():
    destination = Destination.get_all()
    for destination in destinations:
        print(destination)

def find_destination_by_name():
    name = input("Enter the destination's name: ")
    destination = Destination.find_by_name(name)
    print(destination) if destination else print(
        f'Destination {name} not found :(')

def update_destination():
    name = input("Enter the destination's name: ")
    if destination := destination.find_by_name(name):
        try:
            name = input("Enter the destination's new name: ")
            destination.name = name

            destination.update()
            print(f'Success: {destination}')
        except Exception as exc:
            print("Error updating destination: ", exc)
    else:
        print(f'Destination {name} not found')

def delete_destination():
    name = input("Enter the destination's name: ")
    if destination := Destination.find_by_name(name):
        destination.delete()
        print(f'Destination {name} deleted')
    else:
        print(f'Destination {name} not found')

def create_activity():
    name = input("Enter the activity's name: ")
    price = input("Enter the activity's price: ")
    length_of_time = input("Enter the activity's length of time in estimated whole hours")
    planned_ahead = input("Enter whether or not the activity needs to be planned in advance by entering either True (for yes) or False (for no)")
    try:
        activity = Activity.create(name, float(price), int(length_of_time), bool(planned_ahead))
        print(f'Success: {activity}')
    except Exception as exc:
        print("Error creating activity: ", exc)

def list_all_activities_by_name():
    activity = Activity.get_all()
    for activity in Activity:
        print(activity)

def find_activity_by_name():
    name = input("Enter the activity's name: ")
    activity = Activity.find_by_name(name)
    print(activity) if activity else print(
        f'Activity {name} not found :(')

def find_activity_by_price():
    price = input("Enter the activity's price: ")
    activity = Activity.find_by_price(price)
    print(activity) if activity else print(
        f'Activities costing {price} not found :(')

def find_activity_by_length_of_time():
    length_of_time = input("Enter the activity's anticipated length of time: ")
    activity = Activity.find_by_length_of_time(length_of_time)
    print(activity) if activity else print(
        f'Activities lasting {length_of_time} hour(s) not found :(')

def find_activity_by_planned_ahead():
    planned_ahead = input("Enter whether or not the activity needs to be planned in advance (T/F): ")
    activity = Activity.find_by_planned_ahead(planned_ahead)
    print(activity) if activity else print(
        f'Activities requiring advance notice (T/F) {planned_ahead} not found :(')

def update_activity():
    name = input("Enter the activity's name: ")
    if activity := Activity.find_by_name(name):
        try:
            name = input("Enter the activity's new name: ")
            activity.name = name
            price = input("Enter the activity's price: ")
            activity.price = price
            length_of_time = input("Enter the activity's anticipated length of time, in whole hours:")
            planned_ahead = input("Enter whether or not the activity needs to be planned in advance using True or False (True = yes, False = no)")
            destination_name = input("Enter the activity's destination: ")
            activity.destination_name = str(destination_name)

            activity.update()
            print(f'Success: {activity}')
        except Exception as exc:
            print("Error updating activity: ", exc)
    else:
        print(f'Activity {name} not found')

def delete_activity():
    name = input("Enter the activity's name: ")
    if activity := Activity.find_by_name(name):
        activity.delete()
        print(f'Activity {name} deleted')
    else:
        print(f'Activity {name} not found')
        
# A handy dandy tip is using enumerate to iterate with an index in python!
# for i, value in enumerate(values, start=1):
#     		print(i, value)

# For my dogs I can use get_all to get a list of dog objects.  To print them out nicely numbered I can do:
# for i, dog in enumerate(dogs, start=1):
#     		print(f”{i}.  {dog.name}”)

# Now the dogs are printed out with sequential numbers (not their id’s) and the client can select one using that number.

# Since I got the dogs from the backend using .get_all() and iterated through the list as shown above, if the user wants number 3, I know the user wants the third one in that list and I can just grab it from dogs - but the 3rd dog's index in the list is 2 (because the first item in a list is at index 0).  dogs is a list of dog objects, so if the user says "I pick 3" I show them dogs[number_they_picked - 1] and voila!  I have the dog (an object) they wanted with all its attributes available to me to show them!! 