import json

FILE = "data/students.json"

def load_data():
    try:
        with open(FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_student(student):
    data = load_data()
    data.append(student)
    save_data(data)

def view_students():
    return load_data()

def delete_student(roll):
    data = load_data()
    new_data = []

    for student in data:
        if student["roll"] != roll:
            new_data.append(student)

    save_data(new_data)

def search_student(roll):
    data = load_data()
    for student in data:
        if student["roll"] == roll:
            return student
    return None

def update_student(roll):
    data = load_data()
    for student in data:
        if student["roll"] == roll:
            student["name"] = input("Enter new name: ")
            student["branch"] = input("Enter new branch: ")
            save_data(data)
            return True
    return False
