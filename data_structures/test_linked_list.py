"""Tests for linked_list.py"""

import unittest
from data_structures.linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    """Tests for linked lists"""

    test_sequence: list[int] = [1, 2, 4, 8, 16]

    def test_append(self):
        """Test appending to the linked list"""
        llst = LinkedList()
        llst.append(1)
        llst.append(2)
        llst.append(4)
        llst.append(8)
        self.assertEqual(list(llst), [1, 2, 4, 8])
        self.assertEqual(len(llst), 4)

    def test_from_iterable(self):
        """Test creating a linked list from an iterable"""
        llst = LinkedList(self.test_sequence)
        self.assertEqual(list(llst), self.test_sequence)
        self.assertEqual(len(llst), len(self.test_sequence))

    def test_from_iterable_empty(self):
        """Test creating a linked list from an empty iterable"""
        llst = LinkedList([])
        self.assertEqual(list(llst), [])
        self.assertEqual(len(llst), 0)
        llst.append(1)
        self.assertEqual(list(llst), [1])
        self.assertEqual(len(llst), 1)

    def test_from_iterable_single(self):
        """Test creating a linked list from an iterable with a single element"""
        llst = LinkedList([1])
        self.assertEqual(list(llst), [1])
        self.assertEqual(len(llst), 1)
        llst.append(2)
        self.assertEqual(list(llst), [1, 2])
        self.assertEqual(len(llst), 2)

    def test_extend(self):
        """Test extending a linked list from an iterable"""
        llst = LinkedList()
        llst.extend(self.test_sequence)
        self.assertEqual(list(llst), self.test_sequence)
        self.assertEqual(len(llst), len(self.test_sequence))
        llst.extend(self.test_sequence)
        self.assertEqual(list(llst), self.test_sequence + self.test_sequence)
        self.assertEqual(len(llst), len(self.test_sequence) * 2)

    def test_extend_empty(self):
        """Test extending a linked list from an empty iterable"""
        llst = LinkedList()
        llst.extend([])
        llst.extend([])
        llst.extend([])
        self.assertEqual(len(llst), 0)
        self.assertEqual(list(llst), [])
        llst.extend([1])
        self.assertEqual(len(llst), 1)
        self.assertEqual(list(llst), [1])

    def test_prepend(self):
        """Test prepending to a linked list"""
        llst = LinkedList()
        llst.prepend(1)
        llst.prepend(2)
        llst.prepend(4)
        llst.prepend(8)
        self.assertEqual(list(llst), [8, 4, 2, 1])
        self.assertEqual(len(llst), 4)

    def test_get(self):
        """Test retrieving a specific element from a linked list"""
        llst = LinkedList(self.test_sequence)
        self.assertEqual(llst[2], 4)
        self.assertEqual(len(llst), len(self.test_sequence))

    def test_set(self):
        """Test setting a specific element from a linked list"""
        llst = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        test_sequence[2] = 100
        llst[2] = 100
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_len(self):
        """Test getting the length of a linked list"""
        llst = LinkedList(self.test_sequence)
        self.assertEqual(len(llst), len(self.test_sequence))

    def test_remove(self):
        """Test removing an element from a linked list"""
        llst = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        removed = llst.remove(2)
        self.assertEqual(removed, test_sequence[2])
        del test_sequence[2]
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_remove_from_head(self):
        """Test removing an element from the head of a linked list"""
        llst = LinkedList(self.test_sequence)
        removed = llst.remove(0)
        test_sequence = list(self.test_sequence)
        self.assertEqual(removed, test_sequence[0])
        del test_sequence[0]
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_remove_from_tail(self):
        """Test removing an element from the tail of a linked list"""
        llst = LinkedList(self.test_sequence)
        tail_idx = len(llst) - 1
        removed = llst.remove(tail_idx)
        test_sequence = list(self.test_sequence)
        self.assertEqual(removed, test_sequence[tail_idx])
        del test_sequence[tail_idx]
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_insert(self):
        """Test inserting an element into a specific index in a linked list"""
        llst = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        llst.insert(3, 100)
        test_sequence.insert(3, 100)
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_insert_at_head(self):
        """Test inserting an element at the head of a linked list"""
        llst = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        llst.insert(0, 100)
        test_sequence.insert(0, 100)
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_insert_at_tail(self):
        """Test inserting an element at the tail of a linked list"""
        llst = LinkedList(self.test_sequence)
        tail_idx = len(llst)
        test_sequence = list(self.test_sequence)
        llst.insert(tail_idx, 100)
        test_sequence.insert(tail_idx, 100)
        self.assertEqual(list(llst), test_sequence)
        self.assertEqual(len(llst), len(test_sequence))

    def test_bounds_checks(self):
        """Test that errors are raised when attempting to do thing out-of-bounds"""
        llst = LinkedList(self.test_sequence)
        self.assertRaises(IndexError, lambda ll_: ll_.remove(-1), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.remove(len(ll_) + 1), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.get(-1), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.get(len(ll_) + 1), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.insert(-1, 100), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.insert(len(ll_) + 1, 100), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.set(-1, 100), llst)
        self.assertRaises(IndexError, lambda ll_: ll_.set(len(ll_) + 1, 100), llst)

    def test_iter(self):
        """Test the linked list iterator"""
        llst = LinkedList(self.test_sequence)
        self.assertEqual(list(iter(llst)), self.test_sequence)
        self.assertEqual(len(llst), len(self.test_sequence))
