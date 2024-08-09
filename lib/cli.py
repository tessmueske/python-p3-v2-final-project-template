# lib/cli.py
from models.activity import Activity
from models.destination import Destination

from helpers import (
    exit_,
    create_destination,
    list_destinations_by_name,
    find_destination_by_name,
    update_destination,
    delete_destination,
    create_activity,
    list_all_activities_by_name,
    find_activity_by_name,
    update_activity,
    delete_activity,
    list_destination_and_activities,
    list_everything
)

Destination.create_table()
Activity.create_table()

def main():
    while True:
        menu()
        choice = input("➺➺➺➺➺➺➺➺➺➺➺ ")
        if choice == "0":
            exit_()
        elif choice == "1":
            create_destination()
        elif choice == "2":
            list_destinations_by_name()
        elif choice == "3":
            find_destination_by_name()
        elif choice == "4":
            update_destination()
        elif choice == "5":
            delete_destination()
        elif choice == "6":
            create_activity()
        elif choice == "7":
            list_all_activities_by_name()
        elif choice == "8":
            find_activity_by_name()
        elif choice == "9":
            update_activity()
        elif choice == "10":
            delete_activity()
        elif choice == "12":
            list_destination_and_activities()
        elif choice == "12":
            list_everything()
        else:
            print("\n .·:*¨ ¨*:·. \n invalid choice :( select something else? \n .·:*¨ ¨*:·. \n ")

def menu():
    print("\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n\n please select an option! \n")
    print("0. exit \n")
    print("1. create a destination \n")
    print("2. list all destinations by name \n")
    print("3. find a destination by its name \n")
    print("4. update a destination \n")
    print("5. delete a destination \n")
    print("6. create an activity \n")
    print("7. list all activities by name \n")
    print("8. find an activity by its name \n")
    print("9. update an activity \n")
    print("10. delete an activity \n")
    print("11. list one destination and all its activities \n")
    print("11. list all destinations and all their activities \n\n .·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·..·:*¨ ¨*:·. \n ")

if __name__ == "__main__":
    main()