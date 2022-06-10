"""Tests for stack.py"""

import unittest
from data_structures.stack import Stack


class StackTest(unittest.TestCase):
    """Stack tests"""

    def test_push_and_pop_one(self):
        """Test pushing and popping a single item"""
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.push(5)
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(len(stack), 0)

    def test_push_and_pop_multiple(self):
        """Test pushing and popping several items"""
        stack = Stack()
        self.assertEqual(len(stack), 0)
        stack.push(5)
        stack.push(6)
        stack.push(7)
        stack.push(8)
        self.assertEqual(len(stack), 4)
        self.assertEqual(stack.pop(), 8)
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(len(stack), 0)

    def test_peek(self):
        """Test peeking at the next item in the stack"""
        stack = Stack()
        self.assertRaises(IndexError, lambda q: q.peek(), stack)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        stack.push(6)
        self.assertEqual(stack.peek(), 6)
        stack.pop()
        self.assertEqual(stack.peek(), 5)

    def test_peek_and_pop_empty(self):
        """Test that peeking or popping from and empty stack raises and error"""
        stack = Stack()
        self.assertRaises(IndexError, lambda s: s.peek(), stack)
        self.assertRaises(IndexError, lambda s: s.pop(), stack)
        stack.push(1)
        stack.peek()
        stack.pop()
        self.assertRaises(IndexError, lambda s: s.peek(), stack)
        self.assertRaises(IndexError, lambda s: s.pop(), stack)

    def test_from_iterable(self):
        """Test creating a stack from an iterable"""
        test_sequence = [1, 2, 3, 4, 5]
        stack = Stack(test_sequence)
        self.assertEqual(list(stack), list(reversed(test_sequence)))

    def test_extend(self):
        """Test extending a stack from an iterable"""
        stack = Stack()
        test_sequence = [1, 2, 3, 4, 5]
        stack.extend(test_sequence)
        self.assertEqual(list(stack), list(reversed(test_sequence)))

    def test_iter(self):
        """Test the exhausting iterator"""
        stack = Stack()
        self.assertEqual(list(stack), [])
        test_sequence = [1, 2, 3, 4, 5]
        stack.extend(test_sequence)
        self.assertEqual(list(stack), list(reversed(test_sequence)))
        self.assertEqual(list(stack), [])
