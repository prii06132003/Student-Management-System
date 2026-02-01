from student import *

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll = input("Enter roll number: ")
        branch = input("Enter branch: ")

        student = {
            "name": name,
            "roll": roll,
            "branch": branch
        }

        add_student(student)
        print("✅ Student added successfully")

    elif choice == "2":
        students = view_students()
        if not students:
            print("No records found.")
        else:
            for s in students:
                print(s)

    elif choice == "3":
        roll = input("Enter roll to search: ")
        student = search_student(roll)
        if student:
            print(student)
        else:
            print("❌ Student not found")

    elif choice == "4":
        roll = input("Enter roll to update: ")
        if update_student(roll):
            print("✅ Student updated")
        else:
            print("❌ Student not found")

    elif choice == "5":
        roll = input("Enter roll to delete: ")
        delete_student(roll)
        print("✅ Student deleted")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
