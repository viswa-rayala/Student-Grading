# Student Grading System

This project is a simple student grading system built in Python. It allows an admin to log in, enter student grades, remove students, and calculate the average grade for a student.

## Features

- Admin login system
- Add grades for students
- Remove a student from the system
- Calculate the average grade of a student
- Menu-driven interface
- Uses dictionaries and lists to store student data

## Login Credentials

Username: `admin`
Password: `helloworld`

## How to Run

1. Open a terminal in the project folder.
2. Run the program:

```bash
python3 "student grading/student.py"
```

## Menu Options

1. Enter Grades
2. Remove Student
3. Average Grades
4. Exit

## Example

When the program starts, it will ask for the username and password. After a successful login, you can choose an option from the menu.

## Notes

- Student names are used as dictionary keys.
- Each student's grades are stored as a list of integers.
- The average grade is calculated using Python's `statistics.mean()` function.
 