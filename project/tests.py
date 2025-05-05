import unittest
from unittest.mock import patch
import json
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.FILENAME = 'hotels.json'

    @patch('builtins.input', side_effect=["1", "123", "Metro", "Test Location", "4.5", "6"])
    def test_week2_day2_add_hotel(self, mock_input):
        main()
        with open(self.FILENAME, 'r') as file:
            hotels = json.load(file)
            self.assertTrue({'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.5} in hotels)

    @patch('builtins.input', side_effect=["2", "123", "6"])
    def test_week2_day3_delete_hotel(self, mock_input):
        with open(self.FILENAME, 'w') as file:
            json.dump([{'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.5}], file)
        main()
        with open(self.FILENAME, 'r') as file:
            hotels = json.load(file)
            self.assertEqual(len(hotels), 0)

    @patch('builtins.input', side_effect=["3", "123", "4.7", "6"])
    def test_week2_day5_update_rating(self, mock_input):
        with open(self.FILENAME, 'w') as file:
            json.dump([{'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.5}], file)
        main()
        with open(self.FILENAME, 'r') as file:
            hotels = json.load(file)
            self.assertTrue({'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.7} in hotels)

    @patch('builtins.input', side_effect=["4", "6"])
    def test_week2_day3_view_hotel(self, mock_input):
        captured_output = StringIO()
        import sys
        sys.stdout = captured_output
        with open(self.FILENAME, 'w') as file:
            json.dump([{'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.5}], file)
        main()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertIn("ID: 123", printed_output)
        self.assertIn("Metro", printed_output)
        self.assertIn("Test Location", printed_output)
        self.assertIn("4.5", printed_output)

    @patch('builtins.input', side_effect=["5", "123", "6"])
    def test_week2_day5_search_hotel(self, mock_input):
        captured_output = StringIO()
        import sys
        sys.stdout = captured_output
        with open(self.FILENAME, 'w') as file:
            json.dump([{'ID': 123, 'name': "Metro", 'location': "Test Location", 'rating': 4.5}], file)
        main()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertIn("ID: 123", printed_output)
        self.assertIn("Metro", printed_output)
        self.assertIn("Test Location", printed_output)
        self.assertIn("4.5", printed_output)

    @patch('builtins.input', side_effect=["invalid_choice", "6"])
    def test_week2_day2_invalid_choice_integration(self, mock_input):
        captured_output = StringIO()
        import sys
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        printed_output = captured_output.getvalue()
        self.assertIn("Invalid choice", printed_output)
        
if __name__ == '__main__':
    unittest.main()
