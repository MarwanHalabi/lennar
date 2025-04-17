# lennar

## Overview

This project is divided into multiple parts, each with its own functionality related to candidate data processing, filtering, and truck/package assignment, utilizing APIs and MongoDB for data storage and operations. This README provides instructions on how to set up, run, and utilize each part of the project.
---

## Project Structure

```
Lenar_home_assignment/

├── utils/
│   ├── __init__.py
│   ├── utils.py
│
├── part_1/
│   ├── __init__.py
│   ├── class_diagram.md
│   └── class_diagram.png
│
├── part_2/
│   ├── __init__.py
│   ├──app.py
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
|
├── tests/
│   └──__init__.py
│     └── tests_part_two/
│       ├── __init__.py
│       └── test_part_two.py
├── README.md
└── setup.py
```

## Requirements

Make sure you have Python 3.8 or higher installed on your machine. You can check your Python version by running:

```bash
python --version
```

## Installation

### 1 Clone the repository:
```bash
git clone https://github.com/MarwanHalabi/lennar.git
cd lennar
```

### 2 Install the required packages:
```bash
pip install -e .
```

## Connecting to MongoDB

Local MongoDB Setup
### 1 Install MongoDB:

Follow the [MongoDB installation instructions](https://www.mongodb.com/docs/manual/installation/) for your operating system.

### 2 Run MongoDB:

Start the MongoDB server:
```bash
mongod
```
MongoDB Configuration:
Make sure to configure your MongoDB connection details in your code as needed. The default connection is typically mongodb://localhost:27017/


## Part One:

### class diagram:
![Image description](https://github.com/MarwanHalabi/lennar/blob/main/part_one/classDiagram.png
)

### Database schema, MongoDB
#### trucks Collection
```
{
  "_id": "uuid",              // UUID string (auto-generated)
  "length": 10.0,             // Length of the truck in meters
  "width": 5.0,               // Width of the truck in meters
  "height": 4.0,              // Height of the truck in meters
  "is_full": false            // Whether the truck is full or available for new assignments
}

```

#### packages Collection
This collection stores the packages that need to be assigned to trucks.
```
{
  "_id": "uuid",              // UUID string (auto-generated)
  "length": 2.0,              // Length of the package in meters
  "width": 1.0,               // Width of the package in meters
  "height": 1.0,              // Height of the package in meters
  "truck_id": "uuid",         // Nullable, references trucks._id (truck the package is assigned to)
}

```

### Request Flow of assigning Packages to Truck 
1. client send a request to add package ids
2. server receives the request (POST /assign-truck)
3. lookup, fetch and validate package
4. calcualte valuome
5. fetch trucks
6. check if any truck can handle the load -> assign the (first) truck ID to the packages -> return 200.
7. if There is no avilable trick return "delayed until the next day"



### API Endpoints
1. POST /add_truck
Add a new truck to the system.
#### Request Body
```
{
  "length": 10.0,
  "width": 5.0,
  "height": 4.0
}
```
#### Response
```
{
  "id": "mongo_object_id"
}
```

2. POST /add_package
Add a new package to be assigned to a truck.
#### Request Body
```
{
  "length": 10.0,
  "width": 5.0,
  "height": 4.0
}
```
#### Response
```
{
  "id": "mongo_object_id"
}
```

3. POST /assign_truck
This endpoint assigns packages to a truck.

Request:
URL: /assign-truck

Method: POST

Body (JSON):
```
{
  "package_ids": ["package_id_1", "package_id_2"]
}
```
Response:
Success (200):

```
{
  "truck": "truck_id",
  "fill_ratio": 0.85,
  "packages_count": 3
}
```
Failure (404):

```
{
  "message": "No suitable truck found. Packages delayed."
}
```

