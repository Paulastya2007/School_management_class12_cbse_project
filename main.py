import mysql.connector

def connect_to_db():
    """Connect to the MySQL database."""
    return mysql.connector.connect(
        user='root', 
        password='my-secret-pw', 
        host='localhost', 
        database='school_management'
    )
def student_management():
    """Handle student management operations."""
    print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
    print('1. NEW ADMISSION')
    print('2. UPDATE STUDENT DETAILS')
    print('3. ISSUE TC')
    print('4. VIEW STUDENT DETAILS')
    print('5. VIEW TOTAL STUDENT DETAILS')

    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        insert_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        view_student_details()
    elif choice == '5':
        view_total_student_details()
    else:
        print('Invalid choice! Please try again.')

def insert_student():
    """Insert a new student record into the database."""
    sname = input("Enter Student Name: ")
    admno = int(input("Enter Admission No: "))
    dob = input("Enter Date of Birth (yyyy-mm-dd): ")
    cls = input("Enter class for admission: ")
    cty = input("Enter City: ")

    db = connect_to_db()
    cursor = db.cursor()
    sql = ("INSERT INTO student (sname, admno, dob, cls, cty) "
           "VALUES (%s, %s, %s, %s, %s)")
    values = (sname, admno, dob, cls, cty)

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Student record inserted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        db.close()

def update_student():
    """Update a student's details."""
    admno = int(input("Enter Admission No: "))
    new_class = input("Enter new class: ")

    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE student SET cls = %s WHERE admno = %s"
    values = (new_class, admno)

    try:
        cursor.execute(sql, values)
        db.commit()
        print("Student record updated successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        db.close()




def view_student_details():
    """Retrieve and display details of a student by admission number."""
    admno = int(input("Enter Admission No to view details: "))

    db = connect_to_db()
    cursor = db.cursor()
    sql = "SELECT * FROM student WHERE admno = %s"
    value = (admno,)

    try:
        cursor.execute(sql, value)
        result = cursor.fetchone()
        if result:
            print("Student Details:")
            print(f"Name: {result[0]}")
            print(f"Admission No: {result[1]}")
            print(f"Date of Birth: {result[2]}")
            print(f"Class: {result[3]}")
            print(f"City: {result[4]}")
        else:
            print("No student found with that Admission No.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()

def view_total_student_details():
    """Retrieve and display details of all students."""
    db = connect_to_db()
    cursor = db.cursor()
    sql = "SELECT * FROM student"

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("Total Student Details:")
        for row in results:
            print(f"Name: {row[0]}, Admission No: {row[1]}, Date of Birth: {row[2]}, Class: {row[3]}, City: {row[4]}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        db.close()






def delete_student():
    """Delete a student's record."""
    admno = int(input("Enter Admission No to delete: "))

    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM student WHERE admno = %s"
    value = (admno,)

    try:
        cursor.execute(sql, value)
        db.commit()
        print("Student record deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        db.close()

def main_menu():
    """Display the main menu and handle user choices."""
    print('-----------------------------------')
    print('WELCOME TO SCHOOL MANAGEMENT SYSTEM')
    print('-----------------------------------')
    print("1. STUDENT MANAGEMENT")
    print("2. EMPLOYEE MANAGEMENT")
    print("3. FEE MANAGEMENT")
    print("4. EXAM MANAGEMENT")

    choice = int(input("\nEnter your choice (1-4): "))
    if choice == 1:
        student_management()
    elif choice == 2:
        print("Employee management coming soon!")
    elif choice == 3:
        print("Fee management coming soon!")
    elif choice == 4:
        print("Exam management coming soon!")
    else:
        print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main_menu()
