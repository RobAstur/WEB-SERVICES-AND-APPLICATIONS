import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

# Create a cursor object
cursor = db.cursor()

# Create the 'suppliers' database
cursor.execute("CREATE DATABASE suppliers")

# Close the database connection and cursor
cursor.close()
db.close()