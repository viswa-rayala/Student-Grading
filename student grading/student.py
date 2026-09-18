# Description

# Create a student grading system using Python that has the following functionalities:
# 1. Entering the Grades of a student
# 2. Removing a student from the system
# 3. Calculating the average grades of students
# The user should be able to select whether he/she wants to remove a student, enter grades for a
# student or find the average grades.
# Also, perform the following as part of this project:

# There should be a log-in system to allow only admin access to the grading system.
# Make sure you use dictionaries and lists for storing student’s data.
# Use Python functions as much as you can

# Hint: Statistics module might be helpful
import statistics
class student_grading:
    def __init__(self):
        self.students={}
    def login(self):
        username=input("Enter username:")
        password=input("Enter password:")
        if(username=="admin" and password=="helloworld"):
            print("Login Successful")
        else:
            print("Login Failed")
            exit()
    def enter_grades(self):
        name=input("Enter Student name:")
        marks=list(map(int,input("Enter grades:").split()))
        self.students[name]=marks
        print("Grades entered successfully")
    def remove(self):
        name=input("Enetr the student name to be removed:")
        if name in self.students:
            del self.students[name]
            print("Student removed successfully")
        else:
            print("Student not found")
    def average_grades(self):
        name=input("Enter the student name to find average grades:")
        if name in self.students:
            avg=statistics.mean(self.students[name])
            print(f"The average grades of",name," is ",avg)
        else:
            print("Student not found")
    def menu(self):
        while True:
            print("1. Enter Grades")
            print("2. Remove Student")
            print("3. Average Grades")
            print("4. Exit")
            choice=int(input("Enter your choice:"))
            if choice==1:
                self.enter_grades()
            elif choice==2:
                self.remove()
            elif choice==3:
                self.average_grades()
            elif choice==4:
                break
            else:
                print("Invalid choice")
if __name__=="__main__":
    sg=student_grading()
    sg.login()
    sg.menu()
    
    