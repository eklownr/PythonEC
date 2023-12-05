import unittest
import sys

sys.path.insert(1, r'C:\Users\46766\Desktop\Python Course\lecture 21\custom_lib\game_math')

import calcs

# Can also be called with python -m unittest tests.test_calcs
class TestCalcs(unittest.TestCase):
    def test_distance(self):
        x1, y1, x2, y2 = 0, 0, 3, 4
        result = calcs.calculate_distance(x1, y1, x2, y2)
        print(result)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
