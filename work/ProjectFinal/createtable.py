import mysql.connector

# Establish connection to MySQL and use the existing 'suppliers' database
db = mysql.connector.connect(
  host="localhost",        # MySQL server is hosted on localhost
  user="root",             # MySQL username
  password="root",             # MySQL password (empty in this case)
  database="suppliers"     # Connect to the existing 'suppliers' database
)

cursor = db.cursor()

# SQL query to create the 'suppliers' table if it doesn't already exist
sql = """
CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(250),
    email VARCHAR(250),
    phone VARCHAR(20),
    country VARCHAR(100)
)
"""

# Execute the query to create the table
cursor.execute(sql)

# Commit changes (optional but good practice)
db.commit()

db.close()  # Close the database connection
cursor.close()  # Close the cursor