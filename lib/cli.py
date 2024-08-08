# lib/cli.py
from models.activity import Activity
from models.destination import Destination

from helpers import (
    exit_,
    create_destination,
    list_all_destinations_by_name,
    find_destination_by_name,
    update_destination,
    delete_destination,
    create_activity,
    list_all_activities_by_name,
    find_activity_by_name,
    update_activity,
    delete_activity
)

Destination.create_table()
Activity.create_table()

def main():
    while True:
        menu()
        choice = input("... ")
        if choice == "0":
            exit_()
        elif choice == "1":
            create_destination()
        elif choice == "2":
            list_all_destinations_by_name()
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
        else:
            print("Invalid choice :(")

def menu():
    print("please select an option:")
    print("0. exit")
    print("1. create a destination")
    print("2. list all destinations by name")
    print("3. find a destination by its name")
    print("4. update a destination")
    print("5. delete a destination")
    print("6. create an activity")
    print("7. list all activities by name")
    print("8. find an activity by its name")
    print("9. update an activity")
    print("10. delete an activity")

if __name__ == "__main__":
    main()