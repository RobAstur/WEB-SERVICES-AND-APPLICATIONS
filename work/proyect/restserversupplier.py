from flask import Flask, request, jsonify, abort
from supplierDAOskeleton import supplierDAO

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/')
def index():
    return "Supplier Management"

# Get all suppliers
@app.route('/suppliers', methods=['GET'])
def getall():
    return jsonify(supplierDAO.getAll())

# Get supplier by ID
@app.route('/suppliers/<int:id>', methods=['GET'])
def findbyid(id):
    return jsonify(supplierDAO.findByID(id))

# Create a new supplier
@app.route('/suppliers', methods=['POST'])
def create():
    print(">>> Flask /suppliers POST route hit")
    data = request.json
    print(">>> Received data:", data)
    supplier = {}

    required_fields = ["name", "email", "phone", "country"]
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing field: {field}") 
        supplier[field] = data[field]

    return jsonify(supplierDAO.create(supplier))

# Update an existing supplier
@app.route('/suppliers/<int:id>', methods=['PUT'])
def update(id):
    data = request.json
    supplier = {}

    optional_fields = ["name", "email", "phone", "country"]
    for field in optional_fields:
        if field in data:
            supplier[field] = data[field]

    return jsonify(supplierDAO.update(id, supplier))

# Delete a supplier
@app.route('/suppliers/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify(supplierDAO.delete(id))

if __name__ == "__main__":
    app.run(debug=True)
