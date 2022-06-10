"""Stack implementation"""

from typing import Iterable, Iterator, TypeVar, Generic

T = TypeVar("T")  # pylint: disable=invalid-name
IT = TypeVar("IT")  # pylint: disable=invalid-name


class Stack(Generic[T]):
    """Stack implementation"""

    class StackNode(Generic[IT]):
        """The node for each stack value"""

        def __init__(self, value: IT) -> None:
            self.value: IT = value
            self.next: Stack.StackNode | None = None

    def __init__(self, iterable: Iterable[T] | None = None) -> None:
        # Items are added to the head and removed from the tail
        self.head: Stack.StackNode | None = None
        self.length = 0

        if iterable:
            self.extend(iterable)

    def push(self, value: T) -> None:
        """Push a value"""

        node = Stack.StackNode(value)
        if self.head is None:
            # Handle the special case of pushing the first element
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def pop(self) -> T:
        """Pop a value"""
        if self.head is None:
            raise IndexError

        node = self.head
        self.head = self.head.next
        self.length -= 1

        return node.value

    def extend(self, iterable: Iterable[T]) -> None:
        """Push all elements from an iterable"""
        iterator = iter(iterable)
        for value in iterator:
            self.push(value)

    def peek(self) -> T:
        """Peek at the top item in the stack"""
        if self.head is None:
            raise IndexError
        return self.head.value

    def __len__(self) -> int:
        return self.length

    def __iter__(self) -> Iterator[T]:
        """An iterator that pops items from the stack as it iterates"""
        while len(self) > 0:
            yield self.pop()
