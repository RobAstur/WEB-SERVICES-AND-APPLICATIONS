import mysql.connector
import dbconfig as cfg

class SupplierDAO:
    def __init__(self):
        print("Initializing DAO with config:", cfg.mysql)
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None
        self.cursor = None

    def getcursor(self): 
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=cfg.mysql.get('port', 3306)  # optional
            )
            self.cursor = self.connection.cursor()
            return self.cursor
        except Exception as e:
            print("Database connection failed:", e)
            raise

    def closeAll(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except Exception as e:
            print("Error closing resources:", e)

    def getAll(self):
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM supplier"
            cursor.execute(sql)
            results = cursor.fetchall()
            return [self.convertToDictionary(row) for row in results]
        except Exception as e:
            print("Error in getAll:", e)
            return []
        finally:
            self.closeAll()

    def findByID(self, id):
        try:
            cursor = self.getcursor()
            sql = "SELECT * FROM supplier WHERE id = %s"
            values = (id,)
            cursor.execute(sql, values)
            result = cursor.fetchone()
            if result:
                return self.convertToDictionary(result)
            else:
                return None
        except Exception as e:
            print("Error in findByID:", e)
            return None
        finally:
            self.closeAll()

    def create(self, supplier):
        try:
            cursor = self.getcursor()
            sql = "INSERT INTO supplier (name, email, phone, country) VALUES (%s, %s, %s, %s)"
            values = (
                supplier.get("name"),
                supplier.get("email"),
                supplier.get("phone"),
                supplier.get("country")
            )
            cursor.execute(sql, values)
            self.connection.commit()
            supplier["id"] = cursor.lastrowid
            return supplier
        except Exception as e:
            print("Error in create:", e)
            return None
        finally:
            self.closeAll()

    def update(self, id, supplier):
        try:
            cursor = self.getcursor()
            sql = """
                UPDATE supplier
                SET name = %s, email = %s, phone = %s, country = %s
                WHERE id = %s
            """
            values = (
                supplier.get("name"),
                supplier.get("email"),
                supplier.get("phone"),
                supplier.get("country"),
                id
            )
            cursor.execute(sql, values)
            self.connection.commit()
        except Exception as e:
            print("Error in update:", e)
        finally:
            self.closeAll()

    def delete(self, id):
        try:
            cursor = self.getcursor()
            sql = "DELETE FROM supplier WHERE id = %s"
            values = (id,)
            cursor.execute(sql, values)
            self.connection.commit()
            print("Delete done")
        except Exception as e:
            print("Error in delete:", e)
        finally:
            self.closeAll()

    def convertToDictionary(self, resultLine):
        attkeys = ['id', 'name', 'email', 'phone', 'country']
        return {attkeys[i]: resultLine[i] for i in range(len(attkeys))}


# === Usage Example ===
if __name__ == "__main__":
    supplierDAO = SupplierDAO()
    
    # Test: Get all suppliers
    suppliers = supplierDAO.getAll()
    print("Suppliers:", suppliers)

    # Test: Create a new supplier
    new_supplier = {
        "name": "Test Supplier",
        "email": "test@example.com",
        "phone": "123456789",
        "country": "Testland"
    }
    created = supplierDAO.create(new_supplier)
    print("Created:", created)

    # Test: Find by ID
    if created:
        found = supplierDAO.findByID(created["id"])
        print("Found:", found)

    # Test: Delete
    if created:
        supplierDAO.delete(created["id"])
