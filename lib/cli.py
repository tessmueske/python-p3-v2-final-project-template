# lib/cli.py

from helpers import (
    exit_program,
    list_destination_activities,
    list_destinations,
    list_destinations_by_name,
    find_destination_by_name,
    find_destination_by_id,
    create_destination,
    update_destination,
    delete_destination,
    list_activities,
    list_activities_by_name,
    find_activities_by_name,
    find_activity_by_id,
    create_activity,
    update_activity,
    delete_activity
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")

# def main():
#     while True:
#         menu()
#         choice = input("> ")
#         if choice == "0":
#             exit_program()
#         elif choice == "1":
#             list_departments()
#         elif choice == "2":
#             find_department_by_name()
#         elif choice == "3":
#             find_department_by_id()
#         elif choice == "4":
#             create_department()
#         elif choice == "5":
#             update_department()
#         elif choice == "6":
#             delete_department()
#         elif choice == "7":
#             list_employees()
#         elif choice == "8":
#             find_employee_by_name()
#         elif choice == "9":
#             find_employee_by_id()
#         elif choice == "10":
#             create_employee()
#         elif choice == "11":
#             update_employee()
#         elif choice == "12":
#             delete_employee()
#         elif choice == "13":
#             list_department_employees()
#         else:
#             print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")

# def menu():
#     print("Please select an option:")
#     print("0. Exit the program")
#     print("1. List all departments")
#     print("2. Find department by name")
#     print("3. Find department by id")
#     print("4: Create department")
#     print("5: Update department")
#     print("6: Delete department")
#     print("7. List all employees")
#     print("8. Find employee by name")
#     print("9. Find employee by id")
#     print("10: Create employee")
#     print("11: Update employee")
#     print("12: Delete employee")
#     print("13: List all employees in a department")

if __name__ == "__main__":
    main()
