import mysql.connector

def exam_management(db):
    """Display the exam management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO EXAM MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. ADD NEW EXAM')
        print('2. VIEW ALL EXAMS')
        print('3. VIEW EXAM DETAILS BY EXAM ID')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            insert_exam(db)
        elif choice == '2':
            display_all_exams(db)
        elif choice == '3':
            display_exam_by_id(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def insert_exam(db):
    """Insert a new exam into the database."""
    exam_name = input("Enter Exam Name: ")
    exam_date = input("Enter Exam Date (yyyy-mm-dd): ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO exams (exam_name, exam_date) VALUES (%s, %s)"
        cursor.execute(sql, (exam_name, exam_date))
        db.commit()
        print("New exam added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_exams(db):
    """Display all exams in the database."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM exams"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        if results:
            print("\nAll Exam Details:")
            for row in results:
                print(f"Exam ID: {row[0]}, Exam Name: {row[1]}, Exam Date: {row[2]}")
        else:
            print("No exams found.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_exam_by_id(db):
    """Display details of an exam by its exam ID."""
    exam_id = int(input("Enter Exam ID: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM exams WHERE exam_id = %s"
        cursor.execute(sql, (exam_id,))
        result = cursor.fetchone()
        
        if result:
            print(f"\nExam Details for Exam ID {exam_id}:")
            print(f"Exam Name: {result[1]}, Exam Date: {result[2]}")
        else:
            print("No exam found with this ID.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
