import mysql.connector
import pandas as pd


def employee_management(db):
    """Display the employee management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. NEW EMPLOYEE')
        print('2. VIEW ALL EMPLOYEE DETAILS')
        print('3. VIEW EMPLOYEE DETAILS BY EMPLOYEE NUMBER')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            insert_employee(db)
        elif choice == '2':
            display_all_employees(db)
        elif choice == '3':
            display_employee_by_empno(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def insert_employee(db):
    """Insert a new employee into the database."""
    ename = input("Enter Employee Name: ")
    empno = int(input("Enter Employee Number: "))
    job = input("Enter Job Title: ")
    hiredate = input("Enter Hire Date (yyyy-mm-dd): ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO emp (ename, empno, job, hiredate) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (ename, empno, job, hiredate))
        db.commit()
        print("New employee added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_employees(db):
    """Display all employees in the database using Pandas."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()

        if results:
            df = pd.DataFrame(results, columns=['Employee No', 'Name', 'Job Title', 'Hire Date'])
            print(df)
        else:
            print("No employees found.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_employee_by_empno(db):
    """Display details of an employee by their employee number using Pandas."""
    empno = int(input("Enter Employee Number: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM emp WHERE empno = %s"
        cursor.execute(sql, (empno,))
        result = cursor.fetchone()

        if result:
            df = pd.DataFrame([result], columns=['Employee No', 'Name', 'Job Title', 'Hire Date'])
            print(df)
        else:
            print("No employee found with this employee number.")

        input("\nPress any key to continue...")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
