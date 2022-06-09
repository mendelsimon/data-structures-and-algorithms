"""Tests for queue.py"""

import unittest
from data_structures.queue import Queue


class QueueTest(unittest.TestCase):
    """Queue tests"""

    def test_enqueue_and_dequeue_one(self):
        """Test enqueueing and dequeueing a single item"""
        queue = Queue()
        self.assertEqual(len(queue), 0)
        queue.enqueue(5)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(len(queue), 0)

    def test_enqueue_and_dequeue_multiple(self):
        """Test enqueueing and dequeueing several items"""
        queue = Queue()
        self.assertEqual(len(queue), 0)
        queue.enqueue(5)
        queue.enqueue(6)
        queue.enqueue(7)
        queue.enqueue(8)
        self.assertEqual(len(queue), 4)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 6)
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 8)
        self.assertEqual(len(queue), 0)

    def test_peek(self):
        """Test peeking at the next item in the queue"""
        queue = Queue()
        self.assertRaises(IndexError, lambda q: q.peek(), queue)
        queue.enqueue(5)
        self.assertEqual(queue.peek(), 5)
        queue.enqueue(6)
        self.assertEqual(queue.peek(), 5)
        queue.dequeue()
        self.assertEqual(queue.peek(), 6)

    def test_peek_and_dequeue_empty(self):
        """Test that peeking or dequeueing from and empty queue raises and error"""
        queue = Queue()
        self.assertRaises(IndexError, lambda q: q.peek(), queue)
        self.assertRaises(IndexError, lambda q: q.dequeue(), queue)
        queue.enqueue(1)
        queue.peek()
        queue.dequeue()
        self.assertRaises(IndexError, lambda q: q.peek(), queue)
        self.assertRaises(IndexError, lambda q: q.dequeue(), queue)

    def test_from_iterable(self):
        """Test creating a queue from an iterable"""
        test_sequence = [1, 2, 3, 4, 5]
        queue = Queue(test_sequence)
        self.assertEqual(list(queue), test_sequence)

    def test_extend(self):
        """Test extending a queue from an iterable"""
        queue = Queue()
        test_sequence = [1, 2, 3, 4, 5]
        queue.extend(test_sequence)
        self.assertEqual(list(queue), test_sequence)

    def test_iter(self):
        """Test the exhausting iterator"""
        queue = Queue()
        self.assertEqual(list(queue), [])
        test_sequence = [1, 2, 3, 4, 5]
        queue.extend(test_sequence)
        self.assertEqual(list(queue), test_sequence)
        self.assertEqual(list(queue), [])
