import unittest
from day_01_part_02 import calculate_multi


class testPart2(unittest.TestCase):


    def test_1(self):

        self.assertEqual(calculate_multi([14]) , 2)

    
    def test_2(self):
        self.assertEqual(calculate_multi([12 , 14]) , 4)
    

    def test_3(self):
        self.assertEqual(calculate_multi([12 , 14 , 1969]) , 970)
    

    def test_4(self):
        self.assertEqual(calculate_multi([12 , 14 , 1969, 100756]), 51316)
    

    def test_5(self):
        self.assertEqual(calculate_multi([12 , 14 , 1969, 100756 , 154322]) , 128443)
    

if __name__ == '__main__':
    unittest.main()