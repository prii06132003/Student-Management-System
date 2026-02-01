from tkinter import *
from database import *

root = Tk()
root.title("Student Management System")
root.geometry("400x400")

Label(root, text="Student Management System", font=("Arial", 16)).pack(pady=10)

# Inputs
Label(root, text="Roll Number").pack()
roll_entry = Entry(root)
roll_entry.pack()

Label(root, text="Name").pack()
name_entry = Entry(root)
name_entry.pack()

Label(root, text="Branch").pack()
branch_entry = Entry(root)
branch_entry.pack()

# Functions
def add():
    add_student(
        roll_entry.get(),
        name_entry.get(),
        branch_entry.get()
    )
    status_label.config(text="Student Added Successfully")

def view():
    students = get_students()
    result = ""
    for s in students:
        result += f"{s}\n"
    result_label.config(text=result)

def delete():
    delete_student(roll_entry.get())
    status_label.config(text="Student Deleted")

# Buttons
Button(root, text="Add Student", command=add).pack(pady=5)
Button(root, text="View Students", command=view).pack(pady=5)
Button(root, text="Delete Student", command=delete).pack(pady=5)

status_label = Label(root, text="")
status_label.pack(pady=10)

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
