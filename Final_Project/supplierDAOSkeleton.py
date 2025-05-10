# this is a demonstration of the type of function a data layer might have
# Author: Roberto Gomez Garcia 

class SupplierDAO:
    # get all          
    def getAll(self):

        return [{"id": 1, "name": "Supplier One", "email": "one@example.com", "phone": "123456789", "country": "Ireland"}]
    # find by id
    def findByID(self, id):
        return {"id": id, "name": "Supplier One", "email": "one@example.com", "phone": "123456789", "country": "Ireland"}
    # create a book
    def create(self, supplier):
        return {"id": 1, "name": supplier["name"], "email": supplier["email"], "phone": supplier["phone"], "country": supplier["country"]}
    #update a book
    def update(self,id , supplier):
         return {"id": id, "name": supplier.get("name", "Updated Name"), "email": supplier.get("email", "updated@example.com"), "phone": supplier.get("phone", "987654321"), "country": supplier.get("country", "Updated Country")}
    # delete a book of a given id    
    def delete(self, id):
        return True
        
supplierDAO = SupplierDAO()

if __name__ == "__main__":
    supplier = {"id": 1, "name": "Supplier One", "email": "one@example.com", "phone": "123456789", "country": "Ireland"} 
    print("test getall")
    print(f"\t{supplierDAO.getAll()}")
    print("test findById(1)")
    print(f"\t{supplierDAO.findByID(1)}")
    print("test create")
    print(f"\t{supplierDAO.create(supplier)}")
    print("test update")
    print(f"\t{supplierDAO.update(1, supplier)}")
    print("test delete")
    print(f"\t{supplierDAO.delete(1)}")