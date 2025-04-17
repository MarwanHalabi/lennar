from uuid import uuid4

# Truck Model Collection
TRUCKS_COLLECTION = [
    {
        "id": str(uuid4()),
        "length": 20.0,
        "width": 8.0,
        "height": 12.0,
        "is_full": False
    },
    {
        "id": str(uuid4()),
        "length": 18.5,
        "width": 7.5,
        "height": 11.0,
        "is_full": False
    },
    {
        "id": str(uuid4()),
        "length": 25.0,
        "width": 10.0,
        "height": 14.0,
        "is_full": False
    },
    {
        "id": str(uuid4()),
        "length": 22.0,
        "width": 9.0,
        "height": 13.0,
        "is_full": False
    }
]

# Package Model Collection
PACKAGE_COLLECTION = [
    {
        "id": str(uuid4()),
        "length": 5.0,
        "width": 6.0,
        "height": 7.0,
        "truck_id": None  # Not assigned yet
    },
    {
        "id": str(uuid4()),
        "length": 3.0,
        "width": 4.0,
        "height": 5.0,
        "truck_id": None  # Not assigned yet
    },
    {
        "id": str(uuid4()),
        "length": 8.0,
        "width": 6.0,
        "height": 9.0,
        "truck_id": None  # Not assigned yet
    },
    {
        "id": str(uuid4()),
        "length": 6.0,
        "width": 5.0,
        "height": 6.0,
        "truck_id": None  # Not assigned yet
    }
]
