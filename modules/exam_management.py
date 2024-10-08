import mysql.connector
import pandas as pd


def exam_management(db):
    """Display the exam management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO EXAM MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. NEW EXAM RECORD')
        print('2. VIEW ALL EXAM DETAILS')
        print('3. VIEW EXAM DETAILS BY ADMISSION NUMBER')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            insert_exam(db)
        elif choice == '2':
            display_all_exams(db)
        elif choice == '3':
            display_exam_by_admno(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def insert_exam(db):
    """Insert a new exam record into the database."""
    sname = input("Enter Student Name: ")
    admno = int(input("Enter Admission Number: "))
    percentage = float(input("Enter Percentage: "))
    result = input("Enter Result (Pass/Fail): ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO exam (sname, admno, per, res) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (sname, admno, percentage, result))
        db.commit()
        print("New exam record added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_exams(db):
    """Display all exam records in the database using Pandas."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM exam"
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            df = pd.DataFrame(results, columns=['Student Name', 'Admission No', 'Percentage', 'Result'])
            print(df)
        else:
            print("No exam records found.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_exam_by_admno(db):
    """Display exam details by admission number using Pandas."""
    admno = int(input("Enter Admission Number: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM exam WHERE admno = %s"
        cursor.execute(sql, (admno,))
        result = cursor.fetchone()

        if result:
            df = pd.DataFrame([result], columns=['Student Name', 'Admission No', 'Percentage', 'Result'])
            print(df)
        else:
            print("No exam record found for this admission number.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

