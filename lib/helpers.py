# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

#COMPLETED
def exit_():
    print("thanks for planning! happy travels :)")
    exit()

def create_destination():
    name = input("enter the destination's name: ")
    try:
        destination = Destination.create(name)
        print('success!')
    except Exception as exc:
        print("error creating destination! ", exc)

def list_all_destinations_by_name():
    """List all destinations sorted by name."""
    destinations = Destination.get_all()
    print('\n'.join(destination.name for destination in sorted(destinations, key=lambda d: d.name)))

def find_destination_by_name():
    name = input("enter the destination's name: ")
    destination = Destination.find_by_name(name)
    print(destination) if destination else print(
        f'destination {name} not found :(')

def update_destination():
    name = input("enter the destination's name: ")
    if (destination := destination.find_by_name(name)):
        try:
            name = input("enter the destination's new name: ")
            destination.name = name

            destination.update()
            print('success!')
        except Exception as exc:
            print("error updating destination! ", exc)
    else:
        print(f'destination {name} not found :( try again?')

def delete_destination():
    name = input("enter the destination's name: ")
    if destination := Destination.find_by_name(name):
        destination.delete()
        print('deleted!')
    else:
        print(f'destination {name} not found :( try again?')

##########################################

def create_activity():
    name = input("enter the activity's name: ")
    price = input("enter the activity's price: ")
    length_of_time = input("enter the activity's length of time in estimated whole hours")
    plan_ahead = input("enter whether or not the activity needs to be planned in advance by entering either True (for yes) or False (for no)")
    try:
        activity = Activity.create(name, float(price), int(length_of_time), bool(plan_ahead))
        print('success!')
    except Exception as exc:
        print("error creating activity! ", exc)

def list_all_activities_by_name():
    activity = Activity.get_all()
    for activity in Activity:
        print(activity)

def find_activity_by_name():
    name = input("enter the activity's name: ")
    activity = Activity.find_by_name(name)
    print(activity) if activity else print('activity not found :( try again?')

def find_activity_by_price():
    price = input("enter the activity's price in $x.xx format: ")
    activity = Activity.find_by_price(price)
    print(activity) if activity else print(
        f'activities costing {price} not found :( try again?')

def find_activity_by_length_of_time():
    length_of_time = input("enter the activity's anticipated length of time in whole hours: ")
    activity = Activity.find_by_length_of_time(length_of_time)
    print(activity) if activity else print(
        f'activities lasting {length_of_time} hour(s) not found :( try again?')

def find_activity_by_plan_ahead():
    plann_ahead = input("enter whether or not the activity needs to be planned in advance (T/F): ")
    activity = Activity.find_by_plan_ahead(plan_ahead)
    print(activity) if activity else print(
        f'activities requiring advance notice (T/F) {plan_ahead} not found :( try again?')

def update_activity():
    name = input("enter the activity's name: ")
    if activity := Activity.find_by_name(name):
        try:
            name = input("enter the activity's new name: ")
            activity.name = name
            price = input("enter the activity's new price: ")
            activity.price = price
            length_of_time = input("Enter the activity's new anticipated length of time, in whole hours:")
            plan_ahead = input("does the activity needs to be planned in advance? (True = yes, False = no)")
            destination_name = input("enter the activity's destination: ")
            activity.destination_name = destination_name

            activity.update()
            print(f'success! {activity} updated!')
        except Exception as exc:
            print("error updating activity: ", exc)
    else:
        print(f'activity {name} not found :( try again?)')

def delete_activity():
    name = input("enter the activity's name: ")
    if activity := Activity.find_by_name(name):
        activity.delete()
        print(f'activity {name} deleted.')
    else:
        print(f'activity {name} not found :( try again?')