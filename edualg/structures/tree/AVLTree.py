from typing import TypeVar, Generic, Optional, List, Iterable

from edualg.structures.tree.BinarySearchTree import BinarySearchTree

T = TypeVar('T')

class AVLNode(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0


class AVLTree(BinarySearchTree[T]):
    def __init__(self, array: Iterable[T]):
        super().__init__()
        self._root: Optional[AVLNode[T]] = None

        if array:
            for v in array:
                self.insert(v)

    def get_height(self, node: Optional[AVLNode[T]] = None) -> int:
        if node is None:
            return -1
        return node.height

    def update_height(self, node: Optional[AVLNode[T]]) -> None:
        if node is None:
            return
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

    def get_balance(self, node: Optional[AVLNode[T]] = None) -> int:
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def is_balanced(self, node: Optional[AVLNode[T]] = None) -> bool:
        return abs(self.get_balance(node)) <= 1

    def insert(self, value: T):
        self._root = self._insert(value, self._root)

    def _insert(self, value: T, node: Optional[AVLNode[T]] = None) -> AVLNode[T]:
        if node is None:
            return AVLNode(value)

        if value < node.value:
            node.left = self._insert(value, node.left)
        else:
            node.right = self._insert(value, node.right)

        return self.rebalance(node)

    def delete(self, value: T, node: Optional[AVLNode[T]] = None) -> Optional[AVLNode[T]]:
        if node is None:
            node = self._root
        if node is None:
            return None
        return self._delete(value, node)

    def _delete(self, value: T, node: Optional[AVLNode[T]]) -> Optional[AVLNode[T]]:
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            # Найден узел для удаления
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Узел с двумя детьми
                temp = self._get_min(node.right)
                node.value = temp
                node.right = self._delete(temp, node.right)


        return self.rebalance(node)


    def pretty_print(self, node: Optional[AVLNode[T]] = None, prefix: str = "", is_left: bool = True):
        if node is None:
            node = self._root
            if node is None:
                print("Empty tree")
                return

        if node.right:
            self.pretty_print(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + f"{node.value} (h={node.height})")
        if node.left:
            self.pretty_print(node.left, prefix + ("    " if is_left else "│   "), True)

    def rebalance(self, node: Optional[AVLNode[T]] = None) -> Optional[AVLNode[T]]:
        if node is None:
            return None

        self.update_height(node)
        balance = self.get_balance(node)

        # Left Heavy (LL или LR случаи)
        if balance > 1:
            # Left-Right case
            if self.get_balance(node.left) < 0:
                node.left = self.RR(node.left)
            # Left-Left case
            return self.LL(node)

        # Right Heavy (RR или RL случаи)
        if balance < -1:
            # Right-Left case
            if self.get_balance(node.right) > 0:
                node.right = self.LL(node.right)
            # Right-Right case
            return self.RR(node)

        return node

    def LL(self, node: AVLNode[T]) -> AVLNode[T]:
        if node is None or node.left is None:
            return node

        l = node.left
        T2 = l.right

        l.right = node
        node.left = T2

        self.update_height(node)
        self.update_height(l)

        return l

    def RR(self, node: AVLNode[T]) -> AVLNode[T]:
        if node is None or node.right is None:
            return node

        r = node.right
        T2 = r.left

        r.left = node
        node.right = T2

        self.update_height(node)
        self.update_height(r)
        return r