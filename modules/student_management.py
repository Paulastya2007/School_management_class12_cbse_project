import mysql.connector
import pandas as pd

def student_management(db):
    """Display the student management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO STUDENT MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. NEW ADMISSION')
        print('2. VIEW ALL STUDENT DETAILS')
        print('3. VIEW STUDENT DETAILS BY ADMISSION NUMBER')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            insert_student(db)
        elif choice == '2':
            display_all_students(db)
        elif choice == '3':
            display_student_by_admno(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def insert_student(db):
    """Insert a new student into the database."""
    sname = input("Enter Student Name: ")
    admno = int(input("Enter Admission Number: "))
    dob = input("Enter Date of Birth (yyyy-mm-dd): ")
    cls = input("Enter Class: ")
    cty = input("Enter City: ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO student (sname, admno, dob, cls, cty) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (sname, admno, dob, cls, cty))
        db.commit()
        print("Student admission successful!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_students(db):
    """Display all students in the database using Pandas."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            df = pd.DataFrame(results, columns=['Name', 'Admission No', 'DOB', 'Class', 'City'])
            print(df)
        else:
            print("No students found.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
def display_student_by_admno(db):
    """Display details of a student by their admission number using Pandas."""
    admno = int(input("Enter Admission Number: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM student WHERE admno = %s"
        cursor.execute(sql, (admno,))
        result = cursor.fetchone()

        if result:
            df = pd.DataFrame([result], columns=['Name', 'Admission No', 'DOB', 'Class', 'City'])
            print(df)
        else:
            print("No student found with this admission number.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
