from pymongo import MongoClient, ASCENDING
from faker import Faker
from flask import Flask, request, jsonify
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["myDB"]
collection = db["employees"]


# POST /employees route to create a new employee
@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.json  # Get JSON data from the request body
    result = collection.insert_one(data)  # Insert the data into MongoDB
    return jsonify({"id": str(result.inserted_id)}), 201  # Respond with the inserted ID


# Get all employees with optional pagination and sorting
@app.route('/employees', methods=['GET'])
def get_employees():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    sort_by = request.args.get('sort', 'name')

    employees = collection.find().sort(sort_by, ASCENDING).skip((page - 1) * limit).limit(limit)

    employee_list = []
    for employee in employees:
        employee["_id"] = str(employee["_id"])
        employee_list.append(employee)

    return jsonify(employee_list), 200


# Get an employee by ID
@app.route("/employees/<id>", methods=["GET"])
def get_employees_by_id(id):
    query = {"_id": ObjectId(id)}
    employee = collection.find_one(query)
    if employee:
        employee["_id"] = str(employee["_id"])
        return jsonify(employee), 200
    return jsonify({"error": "Employee not found"}), 404


# Update an employee
@app.route("/employees/<id>", methods=["PUT"])
def update_employee(id):
    query = {"_id": ObjectId(id)}
    data = request.json

    result = collection.update_one(query, {"$set": data})
    if result.matched_count > 0:
        return jsonify({"message": "Employee updated"}), 200
    return jsonify({"message": "Employee not found"}), 404


# Delete an employee
@app.route("/employees/<id>", methods=["DELETE"])
def delete_employee(id):
    query = {"_id": ObjectId(id)}
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return jsonify({"message": "employee deleted"}), 200
    return jsonify({"message": "employee not found"}), 404


if __name__ == '__main__':
    app.run(port=5000, debug=True)