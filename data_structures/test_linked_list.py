import unittest
from data_structures.linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    test_sequence: list[int] = [1, 2, 4, 8, 16]
    
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(4)
        ll.append(8)
        self.assertEqual(list(ll), [1, 2, 4, 8])
        self.assertEqual(len(ll), 4)

    def test_from_iterable(self):
        ll = LinkedList(self.test_sequence)
        self.assertEqual(list(ll), self.test_sequence)
        self.assertEqual(len(ll), len(self.test_sequence))

    def test_from_iterable_empty(self):
        ll = LinkedList([])
        self.assertEqual(list(ll), [])
        self.assertEqual(len(ll), 0)
        ll.append(1)
        self.assertEqual(list(ll), [1])
        self.assertEqual(len(ll), 1)

    def test_from_iterable_single(self):
        ll = LinkedList([1])
        self.assertEqual(list(ll), [1])
        self.assertEqual(len(ll), 1)
        ll.append(2)
        self.assertEqual(list(ll), [1, 2])
        self.assertEqual(len(ll), 2)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(4)
        ll.prepend(8)
        self.assertEqual(list(ll), [8, 4, 2, 1])
        self.assertEqual(len(ll), 4)

    def test_get(self):
        ll = LinkedList(self.test_sequence)
        self.assertEqual(ll[2], 4)
        self.assertEqual(len(ll), len(self.test_sequence))

    def test_set(self):
        ll = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        test_sequence[2] = 100
        ll[2] = 100
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_len(self):
        ll = LinkedList(self.test_sequence)
        self.assertEqual(len(ll), len(self.test_sequence))

    def test_remove(self):
        ll = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        removed = ll.remove(2)
        self.assertEqual(removed, test_sequence[2])
        del test_sequence[2]
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_remove_from_head(self):
        ll = LinkedList(self.test_sequence)
        removed = ll.remove(0)
        test_sequence = list(self.test_sequence)
        self.assertEqual(removed, test_sequence[0])
        del test_sequence[0]
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_remove_from_tail(self):
        ll = LinkedList(self.test_sequence)
        tail_idx = len(ll) - 1
        removed = ll.remove(tail_idx)
        test_sequence = list(self.test_sequence)
        self.assertEqual(removed, test_sequence[tail_idx])
        del test_sequence[tail_idx]
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_insert(self):
        ll = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        ll.insert(3, 100)
        test_sequence.insert(3, 100)
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_insert_at_head(self):
        ll = LinkedList(self.test_sequence)
        test_sequence = list(self.test_sequence)
        ll.insert(0, 100)
        test_sequence.insert(0, 100)
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_insert_at_tail(self):
        ll = LinkedList(self.test_sequence)
        tail_idx = len(ll)
        test_sequence = list(self.test_sequence)
        ll.insert(tail_idx, 100)
        test_sequence.insert(tail_idx, 100)
        self.assertEqual(list(ll), test_sequence)
        self.assertEqual(len(ll), len(test_sequence))

    def test_bounds_checks(self):
        ll = LinkedList(self.test_sequence)
        self.assertRaises(IndexError, lambda ll_: ll_.remove(-1), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.remove(len(ll_) + 1), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.get(-1), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.get(len(ll_) + 1), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.insert(-1, 100), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.insert(len(ll_) + 1, 100), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.set(-1, 100), ll)
        self.assertRaises(IndexError, lambda ll_: ll_.set(len(ll_) + 1, 100), ll)

    def test_iter(self):
        ll = LinkedList(self.test_sequence)
        self.assertEqual(list(iter(ll)), self.test_sequence)
        self.assertEqual(len(ll), len(self.test_sequence))