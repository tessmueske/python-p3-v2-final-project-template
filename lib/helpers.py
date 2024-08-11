# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

#COMPLETED
def exit_():
    print(
        " \n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n \nthanks for planning! happy travels :) \n\n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n"
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

def create_activity():
    name = input("enter the activity's name! ")
    price = input("enter the activity's price! ")
    length_of_time = input("enter the activity's length of time in estimated whole hours! ")
    plan_ahead = input("does the activity need to be planned in advance? ")
    destination_name = input("enter the name of the destination for this activity! ")
    destination = Destination.find_by_name(destination_name)
    if destination:
        try:
            activity = Activity.create(name, price, length_of_time, plan_ahead, destination.id)
            print('\n\nsuccess!\n\n')
        except Exception as exc:
            print("\nerror creating activity :( \n", exc)
    else:
        print(f"\ndestination '{destination_name}' not found.... please create the destination first!\n")

def list_all_activities_by_name():
    activities = Activity.get_all()
    for activity in activities:
        print(activity)

def find_activity_by_name():
    name = input("\nenter the activity's name! \n")
    activity = Activity.find_by_name(name)
    print(activity) if activity else print('\nactivity not found :( try again?\n')

def find_activity_by_price():
    price = input("\nenter the activity's price in $0.00 format! \n")
    activity = Activity.find_by_price(price)
    print(activity) if activity else print(
        f'\nactivities costing {price} not found :( try again?\n')

# def find_activity_by_length_of_time():
#     length_of_time = input("enter the activity's anticipated length of time in whole hours! ")
#     activity = Activity.find_by_length_of_time(length_of_time)
#     print(activity) if activity else print(
#         f'activities lasting {length_of_time} hour(s) not found :( try again?')

# def find_activity_by_plan_ahead():
#     plan_ahead = input("enter whether or not the activity needs to be planned in advance (T/F)! ")
#     activity = Activity.find_by_plan_ahead(plan_ahead)
#     print(activity) if activity else print(
#         f'activities requiring advance notice (T/F) {plan_ahead} not found :( try again?')

def update_activity():
    name = input("\nenter the activity's name you want to edit! \n")
    activity = Activity.find_by_name(name)
    if activity:
        try:
            # update name
            new_name = input("\nenter the activity's new name! \n")
            activity.name = new_name
            
            # update price
            price_input = input("\nenter the activity's new price: \n")
            activity.price = float(price_input)
            
            # update length of time
            length_of_time_input = input("\nenter the activity's new anticipated length of time, in whole hours: \n")
            activity.length_of_time = int(length_of_time_input)
            
            # update plan ahead
            plan_ahead = input("\ndoes the activity need to be planned in advance? \n")
            activity.plan_ahead = plan_ahead
            
            # update destination
            destination_name = input("\nenter the activity's destination: \n")
            destination = Destination.find_by_name(destination_name)
            if destination:
                activity.destination_id = destination.id
            else:
                print(f"\ndestination '{destination_name}' not found... make sure it's in the database!\n")
                return
            
            # Save changes
            activity.update()
            print(f"\nsuccess! your activity has been updated :)\n")
        except ValueError as ve:
            print("\nerror updating activity: \n", ve)
        except Exception as exc:
            print("\nerror updating activity: \n", exc)
    else:
        print(f"\nactivity '{name}' not found. try again? (make sure it's in your database!)\n")

def delete_activity():
    name = input("\nenter the activity's name! \n")
    if activity := Activity.find_by_name(name):
        activity.delete()
        print(f'\nactivity {name} deleted!\n')
    else:
        print(f'\nactivity {name} not found :( try again?\n')

def list_destination_and_activities():
    pass

def list_everything():
    pass