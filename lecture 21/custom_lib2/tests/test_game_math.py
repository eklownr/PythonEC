import unittest
import sys
import os 

#folder_path = __file__.split("tests")[0]
#module_path = r"\game_math"
#full_path = folder_path + module_path
#sys.path.insert(1, '../game_math')
#sys.path.insert(1, r"C:\Users\46766\Desktop\Python Course\lecture 21\custom_lib2\game_math")
#print(sys.path)

current_dir = os.path.dirname(__file__) 
parent_dir = os.path.dirname(current_dir) 
game_math_dir = os.path.join(parent_dir, 'game_math') 
sys.path.insert(1, game_math_dir)

from game_physics import calculate_distance

class TestPhysics(unittest.TestCase):
    def test_distance(self):
        x1, y1, x2, y2 = 3, 4, 0, 0
        result = calculate_distance(x1, y1, x2, y2)

        self.assertEqual(result, 6)

