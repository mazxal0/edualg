from typing import TypeVar, Generic, Optional, Iterator

T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, value: T, right: 'Node[T]' = None, left: 'Node[T]' = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'Node({self.value})'

class BaseTree(Generic[T]):
    def __init__(self, _root: 'Node[T]' = None):
        self._root = _root

    @property
    def is_empty(self) -> bool:
        return self._root is None

    def size(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        if node is None:
            return 0

        return 1 + (self.size(node.left) if node.left else 0) + (self.size(node.right) if node.right else 0)

    @property
    def height(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        return max(self._height(node.left), self._height(node.right))

    def _height(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def height_in_vertex(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        return 1 + max(self._height(node.left), self._height(node.right))

    def find(self, value: T, node: Optional[Node[T]]=None) -> Optional[Node[T]]:
        if node is None:
            node = self._root
        if node is None:
            return node

        if node.value == value:
            return node
        left = self.find(value, node.left)
        if left:
            return left
        return self.find(value, node.right)

    def clear(self):
        self._root = None

    def __len__(self) -> int:
        return self.size()

    def __iter__(self) -> Iterator[T]:
        yield from self.inorder()

    def __str__(self) -> str:
        if self.is_empty:
            return "Empty Tree"
        return f'Tree {list(self.inorder())}'

    def __repr__(self) -> str:
        return str(self)

    def __contains__(self, value: T) -> bool:
        return self.find(value) is not None

    def inorder(self, node: Optional[Node[T]]=None) -> Iterator[T]:
        if node is None:
            node = self._root
            if node is None:
                return
        if node.left:
            yield from self.inorder(node.left)
        yield node.value
        if node.right:
            yield from self.inorder(node.right)

    def preorder(self, node: Optional[Node[T]]=None) -> Iterator[T]:
        if node is None:
            node = self._root
        if node is None:
            return
        yield node.value
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

