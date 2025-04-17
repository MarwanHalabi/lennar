from flask import Flask, request, jsonify
from pymongo import MongoClient
from part_two.models import Truck, Package
import logging

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["lennarDB"]
trucks_collection = db["trucks"]
packages_collection = db["packages"]


logger = logging.getLogger(__name__)

# POST AddTruck: Create/store a new truck
@app.route('/add_truck', methods=['POST'])
def add_truck():
    data = request.json
    logger.info(f"Received request to add truck: {data}")
    try:
        truck = Truck(**data) # validate the data types and structe
        truck_data = truck.dict()
        result = trucks_collection.insert_one(truck_data)
        logger.info(f"Truck added with ID: {result.inserted_id}")
        return jsonify({"id": str(result.inserted_id)}), 201

    except Exception as e:
            logger.error(f"Failed to add truck: {str(e)}")
            return jsonify({"error": str(e)}), 400

# POST AddPackage: Create/store new packages.
@app.route('/add_package', methods=['POST'])
def add_package():
    data = request.json
    try:
        package = Package(**data)  # validate the data types and structe
        package_data = package.dict()
        result = packages_collection.insert_one(package_data)
        return jsonify({"id": str(result.inserted_id)}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# POST AssignTruck: Given a list of package IDs, determine if they can be loaded into any
@app.route('/assign_truck', methods=['POST'])
def assign_truck():

    """
    Implement minimal logic to sum up package volumes and compare to truck
    capacity.
    If the chosen truck’s (sum of package volumes) / (truck volume) >= 0.8, consider
    it “full enough” and proceed with the assignment.
    """
    data = request.json
    package_ids = data.get("package_ids", [])
    logger.info(f"Received request to assign packages: {package_ids}")

    if not package_ids:
        return jsonify({"error": "Missing package IDs or truck ID"}), 400

    packages = list(packages_collection.find({"id": {"$in": package_ids}, "truck_id": None}))

    if not packages:
        return jsonify({"error": "Packages not found"}), 404

    total_volume = 0
    for package in packages:
        total_volume += package['length'] * package['width'] * package['height']

    trucks = list(trucks_collection.find({"is_full": False}))
    for truck in trucks:
        truck_volume = truck["length"] * truck["width"] * truck["height"]
        if 0.8 <= total_volume / truck_volume <= 1.0:
            # Update packages with truck ID
            packages_collection.update_many(
                {"id": {"$in": package_ids}},
                {
                    "$set": {
                        "truck_id": truck["_id"],
                    }
                }
            )
            trucks_collection.update_one({"_id": truck["_id"]}, {"$set": {"is_full": True}})

            logger.info(f"Assigned {len(packages)} packages to truck {truck['_id']}")
            return jsonify({"truck": str(truck["_id"]),
                            "fill_ratio": total_volume / truck_volume,
                            "packages_count": len(packages)}), 200

    logger.info("No truck could be filled to 80%. Packages delayed.")
    return jsonify({"message": "No suitable truck found. Packages delayed."}), 200


if __name__ == '__main__':
    app.run(port=5000, debug=True)
