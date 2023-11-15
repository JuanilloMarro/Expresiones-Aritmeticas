from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left: Node | None = None
        self.right: Node | None = None

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None
