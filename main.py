from database import *

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll: ")
        name = input("Name: ")
        branch = input("Branch: ")
        add_student(roll, name, branch)
        print("Student added successfully")

    elif choice == "2":
        for s in get_students():
            print(s)

    elif choice == "3":
        roll = input("Enter roll: ")
        print(search_student(roll))

    elif choice == "4":
        roll = input("Roll: ")
        name = input("New Name: ")
        branch = input("New Branch: ")
        update_student(roll, name, branch)
        print("Updated successfully")

    elif choice == "5":
        roll = input("Roll: ")
        delete_student(roll)
        print("Deleted successfully")

    elif choice == "6":
        break
