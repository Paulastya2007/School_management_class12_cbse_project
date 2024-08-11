import mysql.connector
from mysql.connector import Error

try:
    # Establishing the connection
    connection = mysql.connector.connect(
        host='localhost',  # Assuming you're connecting from the same machine where Docker is running
        port=3306,  # Default MySQL port
        user='root',  # MySQL root user
        password='my-secret-pw'  # MySQL root password you specified
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
