import unittest
from day_01_part_01 import *

class Test_01(unittest.TestCase):

    def test_read_file(self):
        file_path="input_test"
        self.assertEqual(read_file(file_path) , [1023  , 12235 , 456800 , 78654])
    
    def test_calculate_1(self):
        self.assertEqual(calculate_fuel([12]), 2)
    

    def test_calculate_2(self):
        self.assertEqual(calculate_fuel([12, 14]), 4)
    

    def test_calculate_3(self):
        self.assertEqual(calculate_fuel([12, 14 , 1969]) , 658)
    

    def test_calculate_4(self):
        self.assertEqual(calculate_fuel([12, 14 , 1969 , 100756]) , 34241)

    
    def test_calculate_5(self):
        fuels=read_file("input_test")
        self.assertEqual(calculate_fuel(fuels) , 182895)




if __name__ == '__main__':
    unittest.main()

    