
# Importing necessary libraries
import sys
import os
import unittest  # Importing unittest module for writing unit tests
from datetime import date  # Importing date class for handling dates
import pandas as pd  # Importing pandas for data manipulation and testing DataFrames
from geopy.distance import geodesic  # Importing geodesic to calculate distances between coordinates

# Adding the parent directory to the system path, so that modules can be imported from the parent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing functions to be tested from the DiaPredict.hw4 module
from DiaPredict.hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list

###########################################
# Defining a test class that inherits from unittest.TestCase
class TestCoreFunctions(unittest.TestCase):

    # Test case for the count_simba function
    def test_count_simba(self):
        # Test data - list of strings with some occurrences of "Simba"
        strings = [
            "Simba and Nala are lions.",
            "I laugh in the face of danger.",
            "Hakuna matata",
            "Timon, Pumba and Simba are friends, but Simba could eat the other two."
        ]
        # Asserting that count_simba correctly counts the occurrences of "Simba" in the list
        self.assertEqual(count_simba(strings), 3)

    # Test case for the get_day_month_year function
    def test_get_day_month_year(self):
        # Test data - list of dates
        dates = [
            date(2023, 10, 17),
            date(2022, 5, 23),
            date(2024, 12, 1)
        ]
        # Expected output - a DataFrame with columns for day, month, and year
        expected_df = pd.DataFrame({
            'day': [17, 23, 1],
            'month': [10, 5, 12],
            'year': [2023, 2022, 2024]
        })
        # Asserting that the DataFrame returned by get_day_month_year matches the expected DataFrame
        pd.testing.assert_frame_equal(get_day_month_year(dates), expected_df)

    # Test case for the compute_distance function
    def test_compute_distance(self):
        # Test data - list of coordinate pairs (start and end points)
        coords = [
            ((41.23, 23.5), (41.5, 23.4)),
            ((52.38, 20.1), (52.3, 17.8))
        ]
        # Expected output - list of distances in kilometers between each pair of coordinates
        expected_distances = [
            geodesic((41.23, 23.5), (41.5, 23.4)).kilometers,  # Calculated distance for first pair
            geodesic((52.38, 20.1), (52.3, 17.8)).kilometers  # Calculated distance for second pair
        ]
        # Asserting that compute_distance returns the correct list of distances
        self.assertEqual(compute_distance(coords), expected_distances)

    # Test case for the sum_general_int_list function
    def test_sum_general_int_list(self):
        # Test data - nested list of integers
        list_1 = [[2], 4, 5, [1, [2], [3, 5, [7, 8]], 10], 1]
        # Asserting that sum_general_int_list correctly sums all integers in the nested list
        self.assertEqual(sum_general_int_list(list_1), 48)

# Running the unit tests when the script is executed directly
if __name__ == '__main__':
    unittest.main()