from typing import TypeVar, Optional, Tuple, Iterable
from .BaseTree import BaseTree, Node

T = TypeVar('T')
class BinarySearchTree(BaseTree[T]):
    def __init__(self, array: Optional[Iterable[T]] = None):
        super().__init__()
        if array:
            for v in array:
                self.insert(v)

    @staticmethod
    def create(array: Optional[Iterable[T]] = None) -> 'BinarySearchTree[T]':
        return BinarySearchTree(array)

    @property
    def root(self):
        return self._root

    @property
    def min(self) -> Optional[T]:
        node = self._root

        while node.left:
            node = node.left
        return node.value

    def _get_min(self, node: Optional[Node[T]] = None) -> Optional[T]:
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

    def delete(self, value: T, node: Optional[Node[T]] = None) -> Tuple[Optional[Node[T]], bool]:
        if node is None:
            node = self._root
            if node is None:
                return None, False

        if value < node.value:
            if node.left:
                node.left, deleted = self.delete(value, node.left)
            else:
                deleted = False
        elif value > node.value:
            if node.right:
                node.right, deleted = self.delete(value, node.right)
            else:
                deleted = False
        else:
            deleted = True
            # случай 1: нет детей
            if not node.left and not node.right:
                if node == self._root:
                    self._root = None
                return None, True
            # случай 2: только один ребёнок
            if not node.left:
                return node.right, True
            if not node.right:
                return node.left, True
            # случай 3: два ребёнка
            successor = node.right
            while successor.left:
                successor = successor.left
            node.value = successor.value
            node.right, _ = self.delete(successor.value, node.right)

        return node, deleted

    def copy(self) -> 'BinarySearchTree[T]':
        new_bst = BinarySearchTree[T]()
        for v in self:
            new_bst.insert(v)
        return new_bst

