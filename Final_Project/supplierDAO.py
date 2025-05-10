#Library to connect with  SQL
#Dbconfig to host connecttion settings
import mysql.connector
import dbconfig as cfg

#Below code it is used to connect and perform CRUD operations

class SupplierDAO:
    # Initialize the SupplierDAO with database connection settings from the config file
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
        sql = "SELECT * FROM suppliers"  
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM suppliers WHERE id = %s"  
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    #Create a new supplier
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
    #Update the supplier data
    def update(self, id, supplier):
        cursor = self.getcursor()
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
    #Delete supplier
    def delete(self, id):
        cursor = self.getcursor()
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



supplierDAO = SupplierDAO()

