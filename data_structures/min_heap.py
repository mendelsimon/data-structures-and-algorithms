"""Min-heap implementation"""

from typing import Generic, Iterator, TypeVar
from typing_protocols.protocols import Comparable

T = TypeVar("T", bound=Comparable)  # pylint: disable=invalid-name


class MinHeap(Generic[T]):
    """Min-heap implementation"""

    def __init__(self) -> None:
        self.length: int = 0
        self.table: list[T] = []

    def insert(self, value: T) -> None:
        """Insert a value into the min-heap"""
        # Use empty space if we have (from removals), otherwise append
        if len(self.table) == self.length:
            self.table.append(value)
        else:
            self.table[self.length] = value
        idx = self.length
        self.length += 1

        # Bubble up the value
        parent_idx = (idx - 1) // 2
        while idx > 0 and self.table[idx] < self.table[parent_idx]:
            # Swap the value with its parent, then update the indices
            self.table[idx], self.table[parent_idx] = (
                self.table[parent_idx],
                self.table[idx],
            )
            idx = parent_idx
            parent_idx = (idx - 1) // 2

    def remove_min(self) -> T:
        """Remove and return the heap's minimum value"""
        # Check that we have at least one value left
        if self.length == 0:
            raise IndexError

        self.length -= 1
        removed_value = self.table[0]

        # If this is the last element, then no shuffling is necessary
        if self.length == 0:
            return removed_value

        # Put the last element at the top, then bubble it down
        self.table[0] = self.table[self.length]
        idx = 0
        left_child_idx = (idx * 2) + 1
        right_child_idx = (idx * 2) + 2

        # While there is at least one greater child, bubble it down
        while left_child_idx < self.length:
            if (
                right_child_idx < self.length
                and self.table[right_child_idx] < self.table[left_child_idx]
                and self.table[right_child_idx] < self.table[idx]
            ):
                # If there is a right child which is smaller than the left child
                # and smaller than the current value, bubble down right
                self.table[idx], self.table[right_child_idx] = (
                    self.table[right_child_idx],
                    self.table[idx],
                )
                idx = right_child_idx
            elif self.table[left_child_idx] < self.table[idx]:
                # Otherwise, if there's a left child which is smaller than the current value,
                # bubble down left
                self.table[idx], self.table[left_child_idx] = (
                    self.table[left_child_idx],
                    self.table[idx],
                )
                idx = left_child_idx
            else:
                # If neither the right or left children are smaller, we're done bubbling
                break
            left_child_idx = (idx * 2) + 1
            right_child_idx = (idx * 2) + 2

        return removed_value

    def peek(self) -> T:
        """Return the heap's minimum value without removing it"""
        if self.length == 0:
            raise IndexError
        return self.table[0]

    def __iter__(self) -> Iterator[T]:
        """Iterate over all values by removing them one at a time"""
        while self.length > 0:
            yield self.remove_min()

    def __len__(self):
        return self.length
