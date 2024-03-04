import unittest
from main import calculate_distances, normalize_data

class TestCalculateDistances(unittest.TestCase):
    def test_distance_calculation(self):
        office_location = (19.3797208, -99.1940332)
        client_location = {'latitude': 19.432608, 'longitude': -99.133209}
        result = calculate_distances(client_location)
        self.assertAlmostEqual(result, 5.215, places=2)

class TestNormalizeData(unittest.TestCase):
    def test_normalization(self):
        row = 50
        min_value = 0
        max_value = 100
        result = normalize_data(row, min_value, max_value)
        self.assertEqual(result, 0.5)

if __name__ == '__main__':
    unittest.main()
