# 🏫 Student Management System (Python Console App)

This is a simple **Student Management System** built in Python for managing student data in a college setting. It simulates real-world roles: an **Admin** who adds and manages student data, and **Students** who can view their own details.

---

## Features

- **Admin Portal**:
  - Add student with name and roll number
  - Enter student's CGPA
  - View all student details
- **Student Portal**:
  - Login using roll number
  - View name, branch, year, and CGPA (if entered)
- **Auto detection** of:
  - **Year** (based on roll number)
  - **Branch** (based on roll number codes)

---

## Technologies Used

- Python 3
- Regex (re module)
- Console I/O

---

## How to Run

Clone the repository:
   ```bash
   git clone https://github.com/KEERTHI130705/Student-Management-System.git
   cd student-management-system
   ```

## Roll Number Format

  Example: 100523735001
  <br>
  1005 → Valid college code <br>
  23 → Admission year (used to calculate current year) <br>
  735 → Branch code (e.g., 735 = ECE)

## Access Control
    
  - Admin: Can add/view all students and enter CGPA.
  - Students: Can only view their own details using roll number.
