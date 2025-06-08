# Student Database App

A simple desktop application built with **Python Tkinter** and **PostgreSQL** to manage student records.  
Users can add, search, and display student information like name, age, and address through a user-friendly interface.

---

## 🎯 Features

- ✅ Add new student records
- 🔍 Search student by ID
- 📋 Display all student records
- 💾 Stores data in PostgreSQL database

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** – for GUI
- **psycopg2** – PostgreSQL database connector
- **PostgreSQL** – for data storage

---

## 🖥️ Screenshots

<p align="center">
<img src="images\screenshot18.png" width="500">
</p>

<p align="center">
<img src="images\screenshot19.png" width="500">
</p>

---

## 📦 Project Structure

project-folder/
│
├── student.py # GUI and functionality
├── demo.py # (Optional) script to create table
├── README.md




---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-db-app.git
cd student-db-app
```
2. Install Dependencies
```
pip install psycopg2
```


3. PostgreSQL Setup
Make sure PostgreSQL is installed and running.

Create a database (default used: postgres)

Optionally, run create_table() from the script to initialize the STUDENTS table.
```
CREATE TABLE IF NOT EXISTS STUDENTS (
    ID SERIAL PRIMARY KEY,
    NAME TEXT,
    AGE TEXT,
    ADDRESS TEXT
);
```
4. Run the Application
```
python student.py
```

| Column  | Type   | Description       |
| ------- | ------ | ----------------- |
| ID      | SERIAL | Auto-increment ID |
| NAME    | TEXT   | Student's name    |
| AGE     | TEXT   | Student's age     |
| ADDRESS | TEXT   | Student's address |

