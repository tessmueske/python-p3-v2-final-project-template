# lib/helpers.py
from models.activity import Activity
from models.destination import Destination

def exit_():
    print(
        " \n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n \nthanks for planning! happy travels :) \n\n˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚˚ ༘♡ ⋆｡˚\n"
        )
    exit()

def create_destination():
    name = input("\n\nenter the destination's name! ")
    try:
        destination = Destination.create(name)
        print('\n\n ✧･ﾟ: *✧･ﾟ:* \n\n success!\n ✧･ﾟ: *✧･ﾟ:* \n\n')
    except Exception as exc:
        print("\n\nerror creating destination ✎ \n\n", exc)

def list_destinations():
    destinations = Destination.get_all()
    print("\n\nALL DESTINATIONS:")
    for destination in destinations:
        print(f"\n{destination.name}\n ")

def select_dest():
    name = input("\n\nenter the destination's name from the destinations list! ")
    destination = Destination.find_by_name(name)
    if destination:
        print(f"\nname: {destination.name}") 
        return destination
    else:
        print(f'\ndestination {name} not found :(\n')
        return None

def update_destination():
    name = input("\n\n enter the destination's name! ")
    
    if (destination := Destination.find_by_name(name)):
        new_name = input("\n\n enter the new name! ")
        destination.name = new_name
        destination.update()
        print(f"\n\n ✧･ﾟ: *✧･ﾟ:* \n\n updated destination to {destination.name}! \n\n✧･ﾟ: *✧･ﾟ:* \n\n")
    else:
        print("\n\n destination not found :( try again?\n\n")

def delete_destination():
    name = input("\n\nenter the destination's name! \n\n")
    if destination := Destination.find_by_name(name):
        destination.delete()
        print('\n\n deleted! \n\n')
    else:
        print(f'\n\n destination {name} not found :( try again? \n\n')

##########################################


def create_activity(destination):
    name = input("enter the activity's name! \n")
    price = input("enter the activity's price! \n")
    length_of_time = input("enter the activity's length of time in estimated whole hours! \n")
    plan_ahead = input("does the activity need to be planned in advance? \n")
    if destination and destination.id:
        try:
            activity = Activity.create(name, price, length_of_time, plan_ahead, destination.id)
            print('\n\nsuccess!\n\n')
        except Exception as exc:
            print("\nerror creating activity :( \nmore info: ", exc)
    else:
        print("destination not found :( make sure it's in your database already, and remember it's case sensitive. ")

def list_all_activities(destination):
    if destination:
        activities = destination.activities()
        print(f"\ndestination: {destination.name}")
        if activities:
            for activity in activities:
                print(
                    f"\nname: {activity.name}\n "
                    f"price: ${activity.price:.2f}\n"
                    f"length of time: {activity.length_of_time} hours\n "
                    f"plan ahead?: {activity.plan_ahead} \n"
                      )
        else:
            print(f"\nno activities found for {destination.name} :(\n")
    else:
        print("no destination selected.")

def find_activity():
    name = input("\nenter the activity's name! remember that it's case sensitive.\n")
    activity = Activity.find_by_name(name)
    
    if activity:
        destination = Destination.find_by_id(activity.destination_id)
        print(
            f"\ndestination: {destination.name if destination else 'unknown destination'}"
            f"\nname: {activity.name}\n"
            f"price: ${activity.price:.2f}\n"
            f"length of time: {activity.length_of_time} hours\n"
            f"plan ahead?: {activity.plan_ahead}\n"
        )
    else:
        print('\nactivity not found :( try again?\n')

def update_activity(destination):
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
            destination = Destination.find_by_id(destination.id)
            if destination:
                activity.destination_id = destination.id
            else:
                print(f"\ndestination '{destination_name}' not found... make sure it's in the database!\n")
                return
            
            # save changes
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

def list_destination_and_activities(destination):
    destination_name = input("enter the destination name whose associated activities you'd like to see: ")
    destination = Destination.find_by_name(destination_name)
    if destination:
        activities = destination.activities()
        if activities:
            print(f"\nactivities for {destination_name}:")
            for activity in activities:
                print(activity)
        else:
            print(f"no activities found for destination {destination_name} :(")
    else:
        print('destination not found. make sure it is in your database!')

def list_everything():
    destinations = Destination.get_all()
    if destinations:
        for destination in destinations:
            print(f"\ndestination: {destination.name} \n")
            activities = destination.activities()
            if activities:
                print("activities:\n-----------------------")
                for activity in activities:
                    print(f"\nname: {activity.name}\n "
                        f"price: ${activity.price:.2f}\n"
                        f"length of time: {activity.length_of_time} hours\n "
                        f"plan ahead?: {activity.plan_ahead}\n\n********************* \n"
                        )
            else:
                print("none yet!")
    else:
        print("no destinations found :( why don't you try adding one?")