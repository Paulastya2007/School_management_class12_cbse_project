import mysql.connector

def fee_management(db):
    """Display the fee management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO FEE MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. RECORD PAYMENT')
        print('2. VIEW ALL PAYMENTS')
        print('3. VIEW PAYMENT DETAILS BY STUDENT ID')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            record_payment(db)
        elif choice == '2':
            display_all_payments(db)
        elif choice == '3':
            display_payment_by_student_id(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def record_payment(db):
    """Record a new payment into the database."""
    student_id = int(input("Enter Student ID: "))
    amount = float(input("Enter Payment Amount: "))
    payment_date = input("Enter Payment Date (yyyy-mm-dd): ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO payments (student_id, amount, payment_date) VALUES (%s, %s, %s)"
        cursor.execute(sql, (student_id, amount, payment_date))
        db.commit()
        print("Payment recorded successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_payments(db):
    """Display all payments in the database."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM payments"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        if results:
            print("\nAll Payment Details:")
            for row in results:
                print(f"Payment ID: {row[0]}, Student ID: {row[1]}, Amount: {row[2]}, Payment Date: {row[3]}")
        else:
            print("No payments found.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_payment_by_student_id(db):
    """Display details of payments by Student ID."""
    student_id = int(input("Enter Student ID: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM payments WHERE student_id = %s"
        cursor.execute(sql, (student_id,))
        results = cursor.fetchall()
        
        if results:
            print(f"\nPayment Details for Student ID {student_id}:")
            for row in results:
                print(f"Payment ID: {row[0]}, Amount: {row[2]}, Payment Date: {row[3]}")
        else:
            print("No payments found for this student.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
