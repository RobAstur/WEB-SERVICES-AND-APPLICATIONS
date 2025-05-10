import mysql.connector
from mysql.connector import Error

try:
    print("Attempting to connect to MySQL...")
    # Attempting to connect
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""  # Or the correct password
    )

    if db.is_connected():
        print("Successfully connected to MySQL Server")

        cursor = db.cursor()

        # Check if the database exists
        cursor.execute("SHOW DATABASES LIKE 'wsaa'")
        result = cursor.fetchone()
        if not result:
            # Create the database if it does not exist
            cursor.execute("CREATE DATABASE wsaa")
            print("Database 'wsaa' created successfully")
        else:
            print("Database 'wsaa' already exists")

        # Use the 'wsaa' database
        cursor.execute("USE wsaa")

        # Create a table within the 'wsaa' database
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100)
        )
        '''
        cursor.execute(create_table_query)
        print("Table 'users' created successfully in 'wsaa' database")

except mysql.connector.Error as e:
    print(f"Error: {e}")
    if e.errno == 1045:
        print("Access denied: Check username and password.")
    elif e.errno == 2003:
        print("Can't connect to MySQL server: Check MySQL is running and reachable.")
    elif e.errno == 1049:
        print("Unknown database error: This typically happens if MySQL doesn't recognize the database name.")
    else:
        print("An unknown error occurred.")
except Exception as e:
    print(f"General error: {e}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection is closed")
    else:
        print("MySQL connection could not be established.")
