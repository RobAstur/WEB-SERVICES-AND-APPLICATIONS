import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
  host="localhost",
  user="your user",
  password="your password"
)

# Create a cursor object
cursor = db.cursor()

# Create the 'suppliers' database
cursor.execute("CREATE DATABASE suppliers")

# Close the database connection and cursor
cursor.close()
db.close()