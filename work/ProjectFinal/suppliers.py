import mysql.connector

# Connect to MySQL server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = db.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS supplier")

# Use the supplier database
cursor.execute("USE supplier")

# Drop supplier table if it exists
cursor.execute("DROP TABLE IF EXISTS supplier")

# Create supplier table with category
cursor.execute("""
    CREATE TABLE supplier (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(50),
        country VARCHAR(100),
        category VARCHAR(100)
    )
""")

print("Database and supplier table with 'category' column created.")

# Clean up
db.commit()
cursor.close()
db.close()