from typing import TypeVar, Optional
from .BaseTree import BaseTree, Node

T = TypeVar('T')
class BinarySearchTree(BaseTree[T]):
    def __init__(self):
        super().__init__()

    def insert(self, value: T):
        if self._root is None:
            self._root = Node(value)
        else:
            self._insert(value, self._root)

    def _insert(self, value: T, node: Optional[Node[T]]):
        if value < node.value:
            if node.left:
                self._insert(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert(value, node.right)
            else:
                node.right = Node(value)

    def find(self, value: T, node: Optional[Node[T]]=None) -> Optional[T]:
        if node is None:
            node = self._root

        if value == node.value:
            return node
        if value < node.value:
            if node.left:
                return self.find(value, node.left)
        elif value > node.value:
            if node.right:
                return self.find(value, node.right)

        return None

    def delete(self, value: T, node: Optional[Node[T]] = None) -> Optional[T]:
        if node is None:
            node = self._root
        pass
        # TODO

    @property
    def min(self, node: Optional[Node[T]] = None) -> Optional[T]:
        if node is None:
            node = self._root

        while node.left:
            node = node.left
        return node.value

    @property
    def max(self, node: Optional[Node[T]] = None) -> Optional[T]:
        if node is None:
            node = self._root

        while node.right:
            node = node.right
        return node.value

