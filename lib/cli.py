# lib/cli.py
from models.activity import Activity
from models.destination import Destination

from helpers import (
    exit_,
    create_destination,
    list_destinations,
    select_dest,
    update_destination,
    delete_destination,
    create_activity,
    list_all_activities,
    find_activity,
    update_activity,
    delete_activity,
    list_destination_and_activities,
    list_everything
)

# main menu
def main():
    while True:
        dest_menu()
        choice = input("➺➺➺➺➺➺➺➺➺➺➺ ")
        if choice == "list all":
            list_destinations()
            change_dest()
        elif choice == "create":
            create_destination()
        elif choice == "search A":
            find_activity()
        elif choice == "see everything":
            list_everything()
        elif choice == "e":
            exit_()

# change destination menu
def change_dest():
    while True:
        change_dest_menu_option()
        choice = input("➺➺➺➺➺➺➺➺➺➺➺ ")
        if choice == "list all":
            list_destinations()
        elif choice == "select":
            destination = select_dest()
            if destination:
                list_destination_and_activities(destination) 
                activity_menu(destination)
            else:
                print("no destination selected :(")
        elif choice == "update":
            update_destination()
        elif choice == "delete":
            delete_destination()
        elif choice == "create":
            create_destination()
        elif choice == "go back":
            return 
        elif choice == "e":
            exit_()

# activity menu
def activity_menu(destination):
    activity_menu_option()
    while True:
        choice = input("➺➺➺➺➺➺➺➺➺➺➺ ")
        if choice == "create A":
            create_activity(destination) 
        elif choice == "list A":
            list_all_activities(destination) 
        elif choice == "update A":
            update_activity(destination)
        elif choice == "delete A":
            delete_activity(destination)
        elif choice == "go back":
            return 
        elif choice == "e":
            exit_()

def dest_menu():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! (options are case sensitive)\n")
    print("type 'list all' to list all destinations \n")
    print("type 'create' to create a new destination \n")
    print("type 'search A' to search for an activity \n")
    print("type 'see everything' to see all destinations and all activities \n")
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

def change_dest_menu_option():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! \n")
    print("type 'list all' to list all destinations \n")
    print("type 'select' to select a destination \n")
    print("type 'update' to update a destination \n")
    print("type 'delete' to delete a destination \n")
    print ("type 'create' to create a new destination \n")
    print("type 'go back' to go back to the main destinations menu \n")
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

def activity_menu_option():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! \n")
    print("type 'create A' to create an activity \n")
    print("type 'list all A' to list all activities \n")
    print("type 'update A' to update an activity \n")
    print("type 'delete A' to delete an activity \n")
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

if __name__ == "__main__":
    main()