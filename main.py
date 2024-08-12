import os
import sys
import mysql.connector
from modules import student_management, employee_management, fee_management, exam_management

def clear_screen():
    """Clear the console screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def main_menu(db):
    """Display the main menu and handle user input."""
    while True:
        clear_screen()
        print('-----------------------------------')
        print('WELCOME TO SCHOOL MANAGEMENT SYSTEM')
        print('-----------------------------------')
        print("1. STUDENT MANAGEMENT")
        print("2. EMPLOYEE MANAGEMENT")
        print("3. FEE MANAGEMENT")
        print("4. EXAM MANAGEMENT")
        print("5. EXIT")

        try:
            choice = int(input("\nEnter your choice (1-5): "))

            if choice == 1:
                student_management.student_management(db)
            elif choice == 2:
                employee_management.employee_management(db)
            elif choice == 3:
                fee_management.fee_management(db)
            elif choice == 4:
                exam_management.exam_management(db)
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    # Establish MySQL connection
    db = mysql.connector.connect(
        user='root',
        password='my-secret-pw',
        host='localhost',
        database='school_management'
    )

    try:
        main_menu(db)
    finally:
        db.close()