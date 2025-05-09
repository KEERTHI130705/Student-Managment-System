import re

class Student:
    def __init__(self, name, rollno):
        self.rollno = rollno
        self.name = name
        self.cgpa = self.set_cgpa
        self.year = self.set_year()
        self.branch = self.set_branch()

    def set_year(self):
        current_year = 2025
        rollno_str = str(self.rollno)
        if re.match(r'1005', rollno_str[0:4]):
            year = current_year - int('20' + rollno_str[4:6])
            if year == 1:
                return "First Year"
            elif year == 2:
                return "Second Year"
            elif year == 3:
                return "Third Year"
            elif year == 4:
                return "Fourth Year"
            else:
                return "Invalid Year"
        else:
            return "Invalid roll no"

    def set_branch(self):
        code = self.rollno[6:9]
        branch_map = {
            '735': "ECE",
            '736': "Mechanical",
            '729': "AIML",
            '730': "Mining",
            '731': "Biomedical",
            '732': "Civil",
            '733': "CSE",
            '734': "EEE"
        }
        return branch_map.get(code, "Invalid Branch")
    def set_cgpa(self):
        cgpa = input("Enter CGPA: ")
        student_database[self.rollno].cgpa = cgpa
        return cgpa
        


    def display(self):
        print(f"\nName: {self.name}")
        print(f"Roll No: {self.rollno}")
        print(f"Year: {self.year}")
        print(f"Branch: {self.branch}")
        print(f"CGPA: {self.cgpa if self.cgpa else 'Not entered'}")


# Global storage (like a database)
student_database = {}

def admin_portal():
    while True:
        print("\n--- Admin Portal ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Logout")
        print("4. Enter student's CGPA")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student's name: ")
            rollno = input("Enter roll number: ")
            if rollno in student_database:
                print("Student already exists.")
            else:
                student_database[rollno] = Student(name, rollno)
                print("Student added successfully.")
        
        elif choice == '2':
            if not student_database:
                print("No students found.")
            else:
                for s in student_database.values():
                    s.display()
        
        elif choice == '3':
            print("Logging out from Admin Portal.")
            break
        elif choice == '4':
            rollno = input("Enter Student's Roll No: ")
            if rollno in student_database:
                Student.set_cgpa(student_database[rollno])
            else:
                print("Student not found.")
        else:
            print("Invalid choice. Try again.")

def student_portal():
    print("\n--- Student Portal ---")
    rollno = input("Enter your roll number: ")
    student = student_database.get(rollno)
    if student:
        student.display()
    else:
        print("Student not found. Please contact admin.")

def main():
    while True:
        print("\n===== Welcome to Student Management System =====")
        print("1. Admin Login")
        print("2. Student Login")
        print("3. Exit")
        user_type = input("Choose your role (1-3): ")

        if user_type == '1':
            admin_portal()
        elif user_type == '2':
            student_portal()
        elif user_type == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

# Run the system
main()
