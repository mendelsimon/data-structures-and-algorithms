"""Queue implementation"""

from typing import Iterable, Iterator, TypeVar, Generic

T = TypeVar("T")  # pylint: disable=invalid-name
IT = TypeVar("IT")  # pylint: disable=invalid-name


class Queue(Generic[T]):
    """Queue implementation"""

    class QueueNode(Generic[IT]):
        """The node for each queue value"""

        def __init__(self, value: IT) -> None:
            self.value: IT = value
            self.prev: Queue.QueueNode | None = None

    def __init__(self, iterable: Iterable[T] | None = None) -> None:
        # Items are added to the head and removed from the tail
        self.head: Queue.QueueNode | None = None
        self.tail: Queue.QueueNode | None = None
        self.length = 0

        if iterable:
            self.extend(iterable)

    def enqueue(self, value: T) -> None:
        """Enqueue a value"""

        node = Queue.QueueNode(value)
        if self.head is None:
            # Handle the special case of inserting the first element
            self.head = node
            self.tail = node
        else:
            assert self.tail is not None  # Since head and tail are always set together
            self.head.prev = node
            self.head = node
        self.length += 1

    def dequeue(self) -> T:
        """Dequeue a value"""
        if self.tail is None:
            raise IndexError

        node = self.tail
        self.tail = self.tail.prev
        self.length -= 1

        # Handle the special case of dequeueing the last node
        if self.tail is None:
            self.head = None

        return node.value

    def extend(self, iterable: Iterable[T]) -> None:
        """Enqueue all elements from an iterable"""
        iterator = iter(iterable)
        for value in iterator:
            self.enqueue(value)

    def peek(self) -> T:
        """Peek at the next item in the queue"""
        if self.tail is None:
            raise IndexError
        return self.tail.value

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator[T]:
        """An iterator that removes items from the queue as it iterates"""
        while len(self) > 0:
            yield self.dequeue()
