"""
CS3C: # tests cases for assignment 06
Abigail Wong
"""

import random
import unittest

from MedianHeap import MedianHeap
from MinHeap import MinHeap

# problem 1
# make sure heap satisfies heap order property

class MoreMinHeapTestCase(unittest.TestCase):

    def assertIsMinHeap(self, minheap):
        self.assertEqual(len(minheap), len(minheap._heap) - 1,)
        heap = minheap._heap
        n = len(heap)

        for i in range(1, len(heap) // 2 + 1): #checks nodes with at least one child
            left = 2 * i
            right = 2 * i + 1

            if left < n:
                self.assertLessEqual(heap[i], heap[left], f"heap \n"
                     "order violation between index and left child")
            if right < n:
                self.assertLessEqual(heap[i], heap[right], f"heap \n"
                     "order violation between index and right child")

    def test_invalid_left_violation(self):
        class FakeMinHeap:
            def __init__(self):
                self._heap = [None, 10, 5] #10>5 = invalid
            def __len__(self):
                return len(self._heap) - 1

        with self.assertRaises(AssertionError):
            self.assertIsMinHeap(FakeMinHeap())

    def test_invalid_length_violation(self):
        class FakeMinHeap:
            def __init__(self):
                self._heap = [None, 10, 2]
            def __len__(self):
                return 1 #incorrect length

        with self.assertRaises(AssertionError):
            self.assertIsMinHeap(FakeMinHeap())

    def testInsertRemoveRandom(self):
        mh = MinHeap()
        numbers = random.sample(range(1, 5000), 1000)

        for number in numbers:
            mh.insert(number)
            self.assertIsMinHeap(mh)

        sorted_numbers = []
        while len(mh) > 0:
            min_number = mh.remove()
            sorted_numbers.append(min_number)
            self.assertIsMinHeap(mh)

        self.assertEqual(sorted_numbers, sorted(numbers))


class MedianHeapTestCase(unittest.TestCase):
    def test_empty(self):
        mh = MedianHeap()
        with self.assertRaises(IndexError):
            mh.peek()
        with self.assertRaises(IndexError):
            mh.remove()
        self.assertEqual(len(mh), 0)

    def test_one_element(self):
        mh = MedianHeap()
        mh.insert(42)
        self.assertEqual(mh.peek(), 42)
        self.assertEqual(len(mh), 1)
        self.assertEqual(mh.remove(), 42)
        self.assertEqual(len(mh), 0)

    def test_two_elements(self):
        mh = MedianHeap()
        mh.insert(10)
        mh.insert(20)
        self.assertEqual(mh.peek(), 10)
        self.assertEqual(mh.remove(), 10)
        self.assertEqual(mh.remove(), 20)

    def test_three_elements(self):
        mh = MedianHeap()
        mh.insert(10)
        mh.insert(20)
        mh.insert(30)
        self.assertEqual(len(mh), 3)
        self.assertEqual(mh.peek(), 20) #median is 20
        self.assertEqual(mh.remove(), 20)
        self.assertEqual(mh.remove(), 10)
        self.assertEqual(mh.remove(), 30)

if __name__ == '__main__':
    unittest.main()