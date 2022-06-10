"""Tests for min_heap.py"""

import unittest
from data_structures.min_heap import MinHeap


class MinHeapTest(unittest.TestCase):
    """Min-heap tests"""

    def test_add_and_remove(self):
        """Test adding and removing from the min heap"""
        heap = MinHeap()
        heap.insert(2)
        self.assertEqual(heap.remove_min(), 2)
        heap.insert(4)
        heap.insert(1)
        heap.insert(3)
        self.assertEqual(heap.remove_min(), 1)
        self.assertEqual(heap.remove_min(), 3)
        self.assertEqual(heap.remove_min(), 4)

    def test_peek(self):
        """Test peeking at the first element in the min-heap"""
        heap = MinHeap()
        heap.insert(2)
        self.assertEqual(heap.peek(), 2)
        self.assertEqual(heap.peek(), 2)
        heap.insert(4)
        heap.insert(1)
        heap.insert(3)
        self.assertEqual(heap.peek(), 1)
        self.assertEqual(heap.peek(), 1)
        self.assertEqual(heap.remove_min(), 1)
        self.assertEqual(heap.peek(), 2)
        self.assertEqual(heap.remove_min(), 2)
        self.assertEqual(heap.peek(), 3)
        self.assertEqual(heap.remove_min(), 3)
        self.assertEqual(heap.peek(), 4)

    def test_iter(self):
        """Test the min-heap iterator"""
        heap = MinHeap()
        heap.insert(3)
        heap.insert(4)
        heap.insert(1)
        heap.insert(2)
        self.assertEqual(len(heap), 4)
        self.assertEqual(list(heap), [1, 2, 3, 4])
        self.assertEqual(len(heap), 0)
        self.assertEqual(list(heap), [])

    def test_remove_and_peek_empty(self):
        """
        Test that the appropriate errors are raised why trying to
        peek or remove from an empty min-heap
        """
        heap = MinHeap()
        self.assertRaises(IndexError, lambda h: h.peek(), heap)
        self.assertRaises(IndexError, lambda h: h.remove_min(), heap)
        heap.insert(1)
        heap.remove_min()
        self.assertRaises(IndexError, lambda h: h.peek(), heap)
        self.assertRaises(IndexError, lambda h: h.remove_min(), heap)
