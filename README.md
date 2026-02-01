# 🎓 Student Management System

A web-based **Student Management System** built using **Python** and **Flask** that allows users to manage student records efficiently with authentication and database integration.

---

## 🚀 Features

- 🔐 User Login Authentication  
- ➕ Add New Students  
- 📄 View Student Records  
- ✏️ Update Student Details  
- ❌ Delete Student Records  
- 🗄️ SQLite Database Integration  
- 🎨 Clean UI using HTML & CSS  

---

## 🛠️ Technologies Used

- Python  
- Flask  
- SQLite  
- HTML  
- CSS  
- Git & GitHub  

---

## 📁 Project Structure

Student-Management-System/
│
├── app.py
├── main.py
├── database.py
├── gui.py
├── student.py
│
├── templates/
│ ├── login.html
│ └── index.html
│
├── static/
│ └── style.css
│
├── students.db
├── README.md
└── .gitignore


---

## ⚙️ How to Run the Project

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/Student-Management-System.git
cd Student-Management-System
```
### Step 2: Install required packages
pip install flask

### Step 3: Run the application
python app.py

### Step 4: Open in browser
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔐 Login System

- Login system implemented using Flask
- User credentials stored in SQLite database
- Session-based authentication
- Prevents unauthorized access

---

## 🗄️ Database Details
- Database Name: students.db
- Tables:
- users
- username
- password
- students
- roll
- name
- branch
Database is automatically created when the app runs.

---

## 📌 Future Improvements
- Password hashing (bcrypt)
- Role-based login (Admin / User)
- Search & filter students
- Export data to Excel
- Improved UI using Bootstrap

---

## 👨‍💻 Author
Priyanka Mahapatra
Student | Python Developer

---

⭐ Support
If you like this project, don’t forget to star ⭐ the repository!

