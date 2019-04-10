#Name: Eric Pirniakan

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter2(self):
        list1 = [0, 5, 1, 120, 3, -9]
        self.assertEqual(max_list_iter(list1), 120)

    def test_max_list_iter_empty_list(self):
        list2 = []
        self.assertEqual(max_list_iter(list2), None)
        
    def test_max_list_iter_negatives(self):
        list3 = [-113, -50, -9, -45, -89, -1235, -35]
        self.assertEqual(max_list_iter(list3), -9)
        
    def test_max_list_iter5(self):
        list4 = [9, 5, 3, 5, 5, 3, 8]
        self.assertEqual(max_list_iter(list4), 9)
        
    def test_max_list_iter_same_int(self):
        list5 = [1, 2, 3, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(max_list_iter(list5), 10)
        
    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        
    def test_reverse_rec_with_strings(self):
        self.assertEqual(reverse_rec(['Hello', 4, 'Hi', 1, 4, 'Bye']), ['Bye', 4, 1, 'Hi', 4, 'Hello'])
        
    def test_reverse_rec_same_integers(self):
        self.assertEqual(reverse_rec([2, 5, 6, 5, 5, 6, 10, 2]), [2, 10, 6, 5, 5, 6, 5, 2])
        
    def test_reverse_rec_none(self):
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)
            
    def test_reverse_rec_all_same(self):
        self.assertEqual(reverse_rec([9, 9, 9, 9, 9, 9, 9, 9]), [9, 9, 9, 9, 9, 9, 9, 9])


    '''def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
'''
if __name__ == "__main__":
        unittest.main()

    
