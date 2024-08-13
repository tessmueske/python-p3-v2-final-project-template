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
        elif choice == "everything":
            list_everything()
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
        elif choice == "everything":
            list_everything()
        elif choice == "select":
            destination = select_dest()
            activity_menu(destination)
        elif choice == "update":
            update_destination()
        elif choice == "delete":
            delete_destination()
        elif choice == "create":
            create_destination()
        elif choice == "go back":
            main()
        elif choice == "e":
            exit_()

# activity menu
def activity_menu(destination):
    activity_menu_option()
    while True:
        choice = input("➺➺➺➺➺➺➺➺➺➺➺ ")
        if choice == "add A":
            create_activity(destination) 
            activity_menu(destination) 
        elif choice == "list all A":
            list_all_activities(destination) 
            activity_menu(destination) 
        elif choice == "update A":
            update_activity(destination)
            activity_menu(destination) 
        elif choice == "delete A":
            delete_activity()
            activity_menu(destination) 
        elif choice == "go back":
            change_dest()  
        elif choice == "e":
            exit_()

def dest_menu():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! (options are case sensitive)\n")
    print("type 'list all' to list all destinations \n")
    print("type 'everything' to see all destinations and all activities \n")
    print("type 'create' to create a new destination \n")
    print("type 'search A' to search for an activity \n") ############
    print("type 'see everything' to see all destinations and all activities \n")
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

def change_dest_menu_option():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! \n")
    print("type 'list all' to list all destinations \n")
    print("type 'everything' to see all destinations and all activities \n")
    print("type 'select' to select a destination \n")
    print("type 'update' to update a destination's name \n")
    print("type 'delete' to delete a destination \n")
    print ("type 'create' to create a new destination \n") 
    print("type 'go back' to go back to the main menu \n") 
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

def activity_menu_option():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n what do you want to do with this destination? \n")
    print("type 'add A' to add an activity for this destination \n") 
    print("type 'list all A' to list all activities for this destination \n") 
    print("type 'update A' to update an activity for this destination \n") 
    print("type 'delete A' to delete an activity from this destination \n") 
    print("type 'go back' to go back to the main destinations menu \n") 
    print("type 'e' to exit \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n")

if __name__ == "__main__":
    main()