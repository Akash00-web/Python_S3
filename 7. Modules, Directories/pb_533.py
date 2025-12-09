"""
Write a program to build a simple Student Management System using Object Oriented Programming in Python which can perform the following operations:

accept-This method takes details from the user like name, roll number, and marks for two different subjects.

display-This method displays the details of every student.

search-This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number

delete-This method deletes the record of a particular student with a matching roll number.

update-This method updates the roll number of the student. This method will ask for the old roll number and new roll number. It will replace the old roll number with a new roll number.

The following instructions need to be considered while making a program.

1. Give class name as Student
2. Include methods name as accept, display, search, delete and update. (1 mark for each correct method to be formed).
3. Also form constructor with __init__ () method (2 marks for forming constructor).
4. 2 marks for correct object prepared like after deletion of one roll no of student it should update the list with new roll
no. and should display it.
The example is just for understanding but logic should be for any n number of students.For Example:
List of Students
Name : A
RollNo : 1
Marks1 : 100
Marks2 : 100
Name : B
RollNo : 2
Marks1 : 90
Marks2 : 90

"""

class Student:
    students=[]
    def __init__(self):
        self.name = ""
        self.roll = 0
        self.mark1 = 0
        self.mark2 = 0

          
    def accept(self):
        self.name = input("Enter name of student: ")
        self.roll = int(input("Enter roll number: "))
        self.mark1 = int(input("Subject 1 marks: "))
        self.mark2 = int(input("Subject 2 marks: "))
        Student.students.append(self)

    
    def display(self):
        for student in Student.students:
            print(f"Name: {student.name}")
            print(f"Roll No: {student.roll}")
            print(f"Marks1: {student.mark1}")
            print(f"Marks2: {student.mark2}")
            print()
    
    def search(self):
        roll = int(input("Enter roll number to search: "))
        for student in Student.students:
            if student.roll == roll:
                print(f"Name: {student.name}")
                print(f"Roll No: {student.roll}")
                print(f"Marks1: {student.mark1}")
                print(f"Marks2: {student.mark2}")
                return
        print("Student not found")

    def delete(self):
        roll = int(input("Enter roll number to delete: "))
        for i, student in enumerate(Student.students):
            if student.roll == roll:
                Student.students.pop(i)
                print("Student deleted successfully")
                return
        print("Student not found")

    def update(self):
        old_roll = int(input("Enter old roll number: "))
        for student in Student.students:
            if student.roll == old_roll:
                student.roll = int(input("Enter new roll number: "))
                print("Roll number updated successfully")
                return
        print("Student not found")

d=Student()
while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        d.accept()
    elif choice == '2':
        d.display()
    elif choice == '3':
        d.search()
    elif choice == '4':
        d.delete()
    elif choice == '5':
        d.update()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

