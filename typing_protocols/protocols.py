"""Protocols bounds for TypeVars"""

from abc import abstractmethod
from typing import Protocol, TypeVar, Any

C = TypeVar("C")  # pylint: disable=invalid-name


class Comparable(Protocol):
    """Implements __lt__() and __eq__()"""

    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    @abstractmethod
    def __eq__(self: C, other: Any) -> bool:
        pass
