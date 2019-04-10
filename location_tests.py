import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        
    def test_repr2(self):
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc2), "Location('Paris', 48.9, 2.4)")
        
    def test_repr3(self):
        loc3 = Location("Irvine", 33.7, 117.8)
        self.assertEqual(repr(loc3), "Location('Irvine', 33.7, 117.8)")
        
    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc == loc2, True)
        
    def test_eq2(self):
        loc = Location("Paris", 31.3, -120.5)
        loc2 = Location("Paris", 48.9, 2.4)
        self.assertEqual(loc == loc2, False)
        
    def test_eq3(self):
        loc = Location("Paris", 48.9, 2.4)
        loc2 = Location ("Paris", 48.9, 2.4)
        self.assertEqual(loc == loc2, True)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
