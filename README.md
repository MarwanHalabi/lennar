# lennar

## Overview

This project is divided into two parts, each with its own functionality related to candidate data processing and filtering. This README provides instructions on how to set up, run, and utilize each part of the project.

---

## Project Structure

```
Lenar_home_assignment/

├── utils/
│   ├── __init__.py
│   ├── fetch_data_from_url.py
│
├── part_1/
│   ├── __init__.py
│   ├── candidate_data.py
│   ├── extractor.py
│   ├── formatter.py
│   ├── main.py
│   ├── utils.py
│   └── requirements.txt
│
├── part_2/
│   ├── __init__.py
│   ├──filter.py
│   ├── main.py
│   ├── mongo_integrtion.py
│   └── requirements.txt
|
├── tests/
│   └──__init__.py
│     └── tests_part_one/
│       └── test_part_one.py
│     └── tests_part_two/
│       ├── __init__.py
│       ├── test_filter.py
│       ├── test_mongo_integration.py
│       └── test_main.py
│
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
Verify Entry Points: After installation, you should be able to run your scripts using the following commands:

```bash
run-part_one
run-part2
```

If you want to install dependencies for each part individually, navigate to each part's directory and run:
```bash
cd part_one
pip install -r requirements.txt
```
```bash
cd ../part_two
pip install -r requirements.txt
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


## How to Run
### Part One:
Run the main script:

```bash
run-part_one
```
This script will extract and format candidate data as specified.

### Part Two:
Run the main script:
```bash
run-part2
```
This script will filter candidates based on industry, skills, and experience, and store the filtered results in MongoDB.


