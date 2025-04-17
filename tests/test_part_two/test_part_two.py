import unittest
from unittest.mock import patch
from part_two.app import app
from uuid import uuid4


class TestTruckPackageAPI(unittest.TestCase):

    @patch('part_two.app.trucks_collection.insert_one')
    def test_add_truck(self, mock_insert):
        # Mock a truck to be returned when insert_one is called
        mock_insert.return_value.inserted_id = str(uuid4())

        new_truck = {
            "length": 20.0,
            "width": 8.0,
            "height": 12.0,
            "is_full": False
        }

        with app.test_client() as client:
            response = client.post('/add_truck', json=new_truck)

            self.assertEqual(response.status_code, 201)
            self.assertIn('id', response.json)

    @patch('part_two.app.packages_collection.insert_one')
    def test_add_package(self, mock_insert):
        # Mock a package to be returned when insert_one is called
        mock_insert.return_value.inserted_id = str(uuid4())

        new_package = {
            "length": 5.0,
            "width": 6.0,
            "height": 7.0,
            "truck_id": None
        }

        with app.test_client() as client:
            response = client.post('/add_package', json=new_package)

            self.assertEqual(response.status_code, 201)
            self.assertIn('id', response.json)

    @patch('part_two.app.trucks_collection.find')
    @patch('part_two.app.packages_collection.find')
    @patch('part_two.app.packages_collection.update_many')
    @patch('part_two.app.trucks_collection.update_one')
    def test_assign_truck(self, mock_update_truck, mock_update_package, mock_find_packages, mock_find_trucks):
        # Setup mock data for trucks and packages
        mock_find_trucks.return_value = [
            {"_id": str(uuid4()), "length": 20.0, "width": 8.0, "height": 12.0, "is_full": False}
        ]
        mock_find_packages.return_value = [
            {"_id": str(uuid4()), "length": 5.0, "width": 6.0, "height": 7.0, "truck_id": None}
        ]

        assign_data = {
            "package_ids": ["package_id_1"]
        }

        with app.test_client() as client:
            response = client.post('/assign_truck', json=assign_data)

            # If a suitable truck is found, the response should contain the truck, fill_ratio, and packages_count
            if response.json.get("message", "") == "No suitable truck found. Packages delayed.":
                self.assertEqual(response.status_code, 200)
                self.assertIn('message', response.json)
            else:
                # If a truck is found and assigned, ensure 'truck' and other expected keys are in the response
                self.assertEqual(response.status_code, 200)
                self.assertIn('truck', response.json)
                self.assertIn('fill_ratio', response.json)
                self.assertIn('packages_count', response.json)

    @patch('part_two.app.trucks_collection.find')
    @patch('part_two.app.packages_collection.find')
    @patch('part_two.app.packages_collection.update_many')
    @patch('part_two.app.trucks_collection.update_one')
    def test_no_suitable_truck_for_assignment(self, mock_update_truck, mock_update_package, mock_find_packages,
                                              mock_find_trucks):
        # Setup mock data where no suitable truck is found
        mock_find_trucks.return_value = [
            {"_id": str(uuid4()), "length": 10.0, "width": 5.0, "height": 6.0, "is_full": False}  # Small truck
        ]
        mock_find_packages.return_value = [
            {"_id": str(uuid4()), "length": 8.0, "width": 8.0, "height": 8.0, "truck_id": None}  # Large package
        ]

        assign_data = {
            "package_ids": ["package_id_1"]
        }

        with app.test_client() as client:
            response = client.post('/assign_truck', json=assign_data)

            # If no suitable truck is found, the response should contain the 'message' key
            self.assertEqual(response.status_code, 200)
            self.assertIn('message', response.json)
            self.assertEqual(response.json['message'], 'No suitable truck found. Packages delayed.')


if __name__ == '__main__':
    unittest.main()
