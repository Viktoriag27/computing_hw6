# tests/test_utils.py

import unittest
from DiaPredict.utils import helper_function

class TestUtils(unittest.TestCase):

    def test_helper_function(self):
        self.assertEqual(helper_function(), "This is a helper function.")

if __name__ == '__main__':
    unittest.main()
