import mysql.connector
import dbconfig as cfg

class SupplierDAO:
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def getAll(self):
        cursor = self.getcursor()
        # Updated table name here
        sql = "SELECT * FROM suppliers"  # Query for fetching all suppliers
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        # Updated table name here
        sql = "SELECT * FROM suppliers WHERE id = %s"  # Fetch supplier by ID
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def create(self, supplier):
        print(">>> DAO.create called with:", supplier)
        cursor = self.getcursor()
        # Updated table name here
        sql = "INSERT INTO suppliers (name, email, phone, country) VALUES (%s, %s, %s, %s)"
        values = (
            supplier.get("name"),
            supplier.get("email"),
            supplier.get("phone"),
            supplier.get("country")
        )
        cursor.execute(sql, values)
        self.connection.commit()
        print(">>> Commit successful")
        newid = cursor.lastrowid
        supplier["id"] = newid
        self.closeAll()
        return supplier

    def update(self, id, supplier):
        cursor = self.getcursor()
        # Updated table name here
        sql = "UPDATE suppliers SET name=%s, email=%s, phone=%s, country=%s WHERE id = %s"
        values = (
            supplier.get("name"),
            supplier.get("email"),
            supplier.get("phone"),
            supplier.get("country"),
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        # Updated table name here
        sql = "DELETE FROM suppliers WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("Delete successful")

    def convertToDictionary(self, resultLine):
        attkeys = ['id', 'name', 'email', 'phone', 'country']
        supplier = {}
        currentkey = 0
        for attrib in resultLine:
            supplier[attkeys[currentkey]] = attrib
            currentkey += 1
        return supplier


# Instantiate the DAO for later use
supplierDAO = SupplierDAO()

