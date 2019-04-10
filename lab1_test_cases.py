#Name: Eric Pirniakan

import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self): #tests the raising of ValueError when the list = None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_iter2(self): #regular test of function
        list1 = [0, 5, 1, 120, 3, -9]
        self.assertEqual(max_list_iter(list1), 120)

    def test_max_list_iter_empty_list(self): #tests when the list is empty
        list2 = []
        self.assertEqual(max_list_iter(list2), None)
        
    def test_max_list_iter_negatives(self): #tests when every integer in the list is negative
        list3 = [-113, -50, -9, -45, -89, -1235, -35]
        self.assertEqual(max_list_iter(list3), -9)
        
    def test_max_list_iter5(self): #tests when the max number is in the 0th index
        list4 = [9, 5, 3, 5, 5, 3, 8]
        self.assertEqual(max_list_iter(list4), 9)
        
    def test_max_list_iter_same_int(self): #tests when there are multiple occurences of the same integer
        list5 = [1, 2, 3, 10, 10, 10, 10, 10, 10, 10]
        self.assertEqual(max_list_iter(list5), 10)
        
    def test_reverse_rec(self): #basic reverse of 3 integers
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_reverse_rec2(self): #another basic reverse, this time with 6 integers
        self.assertEqual(reverse_rec([6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6])
        
    def test_reverse_rec_with_strings(self): #reversing with strings involved
        self.assertEqual(reverse_rec(['Hello', 4, 'Hi', 1, 4, 'Bye']), ['Bye', 4, 1, 'Hi', 4, 'Hello'])
        
    def test_reverse_rec_same_integers(self): #testing reversing lists with multiple occurences of same integers at different spots rather than consecutively as tested before
        self.assertEqual(reverse_rec([2, 5, 6, 5, 5, 6, 10, 2]), [2, 10, 6, 5, 5, 6, 5, 2])
        
    def test_reverse_rec_none(self): #tests the raising of ValueError when the list is None
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_reverse_rec_size1(self): #tests reverse rec with a list of size 1
        size1_list = [8]
        self.assertEqual(reverse_rec(size1_list), [8])

    def test_reverse_rec_size2(self): #tests reverse rec with a list of size 2
        size2_list = [8, 24]
        self.assertEqual(reverse_rec(size2_list), [24, 8])

    def test_reverse_rec_empty(self):
        empty_list = []
        self.assertEqual(reverse_rec(empty_list), None)
            
    def test_reverse_rec_all_same(self): #tests reversing the list when every single element is the same integer
        self.assertEqual(reverse_rec([9, 9, 9, 9, 9, 9, 9, 9]), [9, 9, 9, 9, 9, 9, 9, 9])

    def test_bin_search(self): #basic binary search test
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        
    def test_bin_search_empty(self): #tests when binary search is ran on an empty list
        list_val = []
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
        
    def test_bin_search_none(self): #tests the raising of ValueError for a list that is None
        tlist = None
        with self.assertRaises(ValueError):  #used to check for exception
            bin_search(1, 0, 5, tlist)
            
    def test_bin_search_even(self): #tests binary search on a list with an even amount of elements
        list_val2 = [1, 2, 8, 15, 25, 59]
        low = 0
        high = len(list_val2)-1
        self.assertEqual(bin_search(2, 0, len(list_val2)-1, list_val2), 1)
     
    def test_bin_search_repeated_numbers(self): #tests repeated numbers, it returns the first occurrence of the repeated number
        list_val = [2, 5, 5, 5, 5, 7, 10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), 3)
        
    def test_bin_search_not_in_list(self): #tests binary search for a value that is not in the list
        list_val = [12, 32, 52, 82, 102]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
        
    def test_bin_search_lower_half(self): #tests binary search on a target that is in the lower half of a list
        list_val = [10, 20, 30, 40, 50, 60, 70]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(20, 0, len(list_val)-1, list_val), 1)
        
    def test_bin_search_upper_half(self): #tests binary search on a target that is in the upper half of a list
        list_val = [10, 20, 30, 40, 50, 60, 70]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(60, 0, len(list_val)-1, list_val), 5)
    
    def test_bin_search_with_different_low_and_high(self): #tests binary search with a low greater than 0 and high less than the length of the list minus 1
        list_val = [2, 3, 8, 23, 24, 32, 33]
        low = 2
        high = len(list_val)-2 
        self.assertEqual(bin_search(23, 2, len(list_val)-2, list_val), 3)
    
if __name__ == "__main__":
        unittest.main()

    
