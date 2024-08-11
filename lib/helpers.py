# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

#COMPLETED
def exit_():
    print(
        " \n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n thanks for planning! happy travels :) \n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n"
        )
    exit()

#COMPLETED
def create_destination():
    name = input("\n\nenter the destination's name! ")
    try:
        destination = Destination.create(name)
        print('\n\n ✧･ﾟ: *✧･ﾟ:* \n\n success!\n ✧･ﾟ: *✧･ﾟ:* \n\n')
    except Exception as exc:
        print("\n\nerror creating destination ✎ \n\n", exc)

#COMPLETED
def list_destinations_by_name():
    destinations = Destination.get_all()
    for destination in destinations:
        print(destination)

#COMPLETED
def find_destination_by_name():
    name = input("\n\nenter the destination's name! ")
    destination = Destination.find_by_name(name)
    print(destination) if destination else print(
        f'\ndestination {name} not found :(\n')

#COMPLETED
def update_destination():
    name = input("\n\n enter the destination's name! ")
    
    if (destination := Destination.find_by_name(name)):
        new_name = input("\n\n enter the new name! ")
        destination.name = new_name
        destination.update()
        print(f"\n\n ✧･ﾟ: *✧･ﾟ:* \n\n updated destination to {destination.name}! \n\n✧･ﾟ: *✧･ﾟ:* \n\n")
    else:
        print("\n\n destination not found :( try again?\n\n")

#COMPLETED
def delete_destination():
    name = input("\n\nenter the destination's name! \n\n")
    if destination := Destination.find_by_name(name):
        destination.delete()
        print('\n\n deleted! \n\n')
    else:
        print(f'\n\n destination {name} not found :( try again? \n\n')

##########################################

# def create_activity():
#     name = input("enter the activity's name! ")
#     price = input("enter the activity's price! ")
#     length_of_time = input("enter the activity's length of time in estimated whole hours! ")
#     plan_ahead = input("enter whether or not the activity needs to be planned in advance by entering either True (for yes) or False (for no)! ")
#     destination_name = input("enter the name of the destination for this activity! ")
#     try:
#         activity = Activity.create(name, price, length_of_time, plan_ahead, destination_name)
#         print('success!')
#     except Exception as exc:
#         print("error creating activity :( ", exc)

def create_activity():
    name = input("enter the activity's name! ")
    price = input("enter the activity's price! ")
    length_of_time = input("enter the activity's length of time in estimated whole hours! ")
    plan_ahead = input("enter whether or not the activity needs to be planned in advance by entering either True (for yes) or False (for no)! ")
    destination_name = input("enter the name of the destination for this activity! ")
    destination = Destination.find_by_name(destination_name)
    if destination:
        try:
            activity = Activity.create(name, price, length_of_time, plan_ahead, destination.id)
            print('success!')
        except Exception as exc:
            print("error creating activity :( ", exc)
    else:
        print(f"destination '{destination_name}' not found.... please create the destination first!")


def list_all_activities_by_name():
    activities = Activity.get_all()
    for activity in activities:
        print(activity)

def find_activity_by_name():
    name = input("enter the activity's name! ")
    activity = Activity.find_by_name(name)
    print(activity) if activity else print('activity not found :( try again?')

def find_activity_by_price():
    price = input("enter the activity's price in $0.00 format! ")
    activity = Activity.find_by_price(price)
    print(activity) if activity else print(
        f'activities costing {price} not found :( try again?')

def find_activity_by_length_of_time():
    length_of_time = input("enter the activity's anticipated length of time in whole hours! ")
    activity = Activity.find_by_length_of_time(length_of_time)
    print(activity) if activity else print(
        f'activities lasting {length_of_time} hour(s) not found :( try again?')

def find_activity_by_plan_ahead():
    plann_ahead = input("enter whether or not the activity needs to be planned in advance (T/F)! ")
    activity = Activity.find_by_plan_ahead(plan_ahead)
    print(activity) if activity else print(
        f'activities requiring advance notice (T/F) {plan_ahead} not found :( try again?')

def update_activity():
    name = input("enter the activity's name! ")
    if activity := Activity.find_by_name(name):
        try:
            name = input("enter the activity's new name! ")
            activity.name = name
            price = input("enter the activity's new price! ")
            activity.price = price
            length_of_time = input("enter the activity's new anticipated length of time, in whole hours! ")
            activity.length_of_time = length_of_time
            plan_ahead = input("does the activity needs to be planned in advance? (True = yes, False = no) ")
            activity.plan_ahead = plan_ahead
            destination_name = input("enter the activity's destination! ")
            activity.destination_name = destination.id

            activity.update()
            print(f'success! {activity} updated!')
        except Exception as exc:
            print("error updating activity: ", exc)
    else:
        print(f'activity {name} not found :( try again?)')

def delete_activity():
    name = input("enter the activity's name! ")
    if activity := Activity.find_by_name(name):
        activity.delete()
        print(f'activity {name} deleted!')
    else:
        print(f'activity {name} not found :( try again?')

def list_destination_and_activities():
    pass

def list_everything():
    pass