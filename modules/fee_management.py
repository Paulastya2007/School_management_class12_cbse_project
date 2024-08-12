import mysql.connector

def fee_management(db):
    """Display the fee management menu and handle user input."""
    while True:
        print('\n---------------------------------')
        print('WELCOME TO FEE MANAGEMENT SYSTEM')
        print('---------------------------------')
        print('1. NEW FEE RECORD')
        print('2. VIEW ALL FEE DETAILS')
        print('3. VIEW FEE DETAILS BY ADMISSION NUMBER')
        print('4. RETURN TO MAIN MENU')

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            insert_fee(db)
        elif choice == '2':
            display_all_fees(db)
        elif choice == '3':
            display_fee_by_admno(db)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def insert_fee(db):
    """Insert a new fee record into the database."""
    admno = int(input("Enter Admission Number: "))
    fee_amount = float(input("Enter Fee Amount: "))
    month = input("Enter Month: ")

    try:
        cursor = db.cursor()
        sql = "INSERT INTO fee (admno, fee, month) VALUES (%s, %s, %s)"
        cursor.execute(sql, (admno, fee_amount, month))
        db.commit()
        print("New fee record added successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        db.rollback()
    finally:
        cursor.close()

def display_all_fees(db):
    """Display all fee records in the database."""
    try:
        cursor = db.cursor()
        sql = "SELECT * FROM fee"
        cursor.execute(sql)
        results = cursor.fetchall()
        
        if results:
            print("\nAll Fee Details:")
            for row in results:
                print(f"Admission No: {row[0]}, Fee: {row[1]}, Month: {row[2]}")
        else:
            print("No fee records found.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def display_fee_by_admno(db):
    """Display fee details by admission number."""
    admno = int(input("Enter Admission Number: "))

    try:
        cursor = db.cursor()
        sql = "SELECT * FROM fee WHERE admno = %s"
        cursor.execute(sql, (admno,))
        result = cursor.fetchone()
        
        if result:
            print(f"\nFee Details for Admission No {admno}:")
            print(f"Admission No: {result[0]}, Fee: {result[1]}, Month: {result[2]}")
        else:
            print("No fee record found for this admission number.")
        
        input("\nPress any key to continue...")  # Pause after displaying the details
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
