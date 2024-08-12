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

        print('{:^40}'.format('WELCOME TO SCHOOL MANAGEMENT SYSTEM'))  # Centered heading
        print('{:^40}'.format('-' * 40))  # Horizontal line

        print("{:3}. STUDENT MANAGEMENT".format(1))
        print("{:3}. EMPLOYEE MANAGEMENT".format(2))
        print("{:3}. FEE MANAGEMENT".format(3))
        print("{:3}. EXAM MANAGEMENT".format(4))
        print("{:3}. EXIT".format(5))

        try:
            choice = int(input("\n{:>20} (1-5): ".format("Enter your choice")))

            if choice == 1:
                student_management.student_management(db)
            elif choice == 2:
                employee_management.employee_management(db)
            elif choice == 3:
                fee_management.fee_management(db)
            elif choice == 4:
                exam_management.exam_management(db)
            elif choice == 5:
                print("\nExiting the program. Goodbye!")
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
