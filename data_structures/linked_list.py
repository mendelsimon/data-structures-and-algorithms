from typing import Iterable, TypeVar, Generic

T = TypeVar('T')

class LinkedListNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.next: LinkedListNode[T]|None = None

class LinkedList(Generic[T]):
    def __init__(self, iterable: Iterable|None = None) -> None:
        self.head: LinkedListNode[T]|None = None
        self.tail: LinkedListNode[T]|None = None
        self.length: int = 0

        if iterable:
            self._init_from_iterable(iterable)

    def _init_from_iterable(self, iterable: Iterable):
        iterator = iter(iterable)
        
        # Set up the head and tail
        try:
            data = next(iterator)
        except StopIteration:
            return self
        node = LinkedListNode(data)
        self.head = node
        self.tail = node
        self.length = 1

        # Append the rest of the data to the LinkedList
        while True:
            try:
                data = next(iterator)
            except StopIteration:
                # Return the LinkedList once all the data has been added to it
                return self
            prev_node = node
            node = LinkedListNode(data)
            prev_node.next = node
            self.tail = node
            self.length += 1

    def append(self, data: T) -> None:
        """Add data to the end of the LinkedList"""
        if self.head is None:
            # Handle the special case of adding the first node
            self.head = LinkedListNode(data)
            self.tail = self.head
        else:
            # Handle the typical case
            assert self.tail is not None
            self.tail.next = LinkedListNode(data)
            self.tail = self.tail.next
        self.length += 1

    def prepend(self, data: T) -> None:
        """Add data to the start of the LinkedList"""
        # Handle the special case of adding the first node
        if self.head is None:
            return self.append(data)

        prev_head = self.head
        self.head = LinkedListNode(data)
        self.head.next = prev_head
        self.length += 1
        
    def remove(self, idx: int) -> T:
        """Remove and return the element at the given index"""
        # Make sure the index is not out-of-bounds
        if idx < 0 or idx > self.length - 1:
            raise IndexError('idx out of bounds')

        self.length -= 1

        # Handle the special case of removing the head
        if idx == 0:
            assert self.head is not None # Due to our bounds check
            node = self.head
            self.head = self.head.next
            return node.data
        
        node_before_idx = self._get_node(idx - 1)

        # Retrieve the data and remove the node
        assert node_before_idx is not None # Due to the bounds check inside _get_node()

        # Handle the special case of removing the tail
        if node_before_idx.next.next is None:
            self.tail = node_before_idx

        data = node_before_idx.next.data
        node_before_idx.next = node_before_idx.next.next
        
        return data

    def insert(self, idx: int, data: T) -> None:
        """Insert data at the given index"""
        # Make sure the index is not out-of-bounds
        if idx < 0 or idx > self.length:
            raise IndexError('idx out of bounds')
        
        # Handle the special cases of inserting at the head or tail
        if idx == 0:
            return self.prepend(data)
        elif idx == self.length:
            return self.append(data)

        node = self._get_node(idx - 1)
        prev_next = node.next
        node.next = LinkedListNode(data)
        node.next.next = prev_next
        self.length += 1

    def get(self, idx: int) -> T:
        """Get the value at the given index"""
        node = self._get_node(idx)
        return node.data

    def set(self, idx: int, data: T) -> None:
        """Set the value for an existing given index"""
        node = self._get_node(idx)
        node.data = data

    def _get_node(self, idx: int):
        """Get the node at the given index"""
        # Make sure the index is not out-of-bounds
        if idx < 0 or idx > self.length - 1:
            raise IndexError('idx out of bounds')
        
        # Find the node at idx
        node = self.head
        for _ in range(idx):
            assert node is not None
            node = node.next

        return node

    def __getitem__(self, idx: int) -> T:
        return self.get(idx)

    def __setitem__(self, idx: int, data: T) -> None:
        return self.set(idx, data)

    def __iter__(self) -> 'LinkedListNodeIterator':
        return LinkedListNodeIterator(self.head)

    def __len__(self) -> int:
        return self.length

class LinkedListNodeIterator:
    def __init__(self, node: LinkedListNode[T]|None) -> None:
        self.node: LinkedListNode[T]|None = node

    def __next__(self):
        if self.node is None:
            raise StopIteration
        data = self.node.data
        self.node = self.node.next
        return data

    def __iter__(self):
        return LinkedListNodeIterator(self.node)
