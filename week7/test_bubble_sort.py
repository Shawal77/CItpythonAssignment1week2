import unittest
#import timeit
from bubble_sort import bubble_sort,optimised_bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bsort(self):
        data = [9,8,7,6,4,5,3,1,2]
        self.assertEqual(bubble_sort(data), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bsort2(self):
        data = [-2,45,0,11,-9]
        self.assertEqual(bubble_sort(data), [-9,-2,0,11,45])
    def test_bsort(self):
        data = [9,8,7,6,4,5,3,1,2]
        self.assertEqual(optimised_bubble_sort(data), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bsort2(self):
        data = [-2,45,0,11,-9]
        self.assertEqual(optimised_bubble_sort(data), [-9,-2,0,11,45])


if __name__ == '__main__':
    unittest.main()
