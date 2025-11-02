from typing import TypeVar, Generic, Optional, Iterator, Iterable, List, Tuple

from edualg.structures.linear import Queue

class NonFindError(Exception):
    pass

T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, value: T, right: 'Node[T]' = None, left: 'Node[T]' = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'Node({self.value})'

class BaseTree(Generic[T]):
    def __init__(self, _root: 'Node[T]' = None) -> None:
        self._root = _root

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

    def __bool__(self) -> bool:
        return self.is_empty

    @property
    def is_empty(self) -> bool:
        return self._root is None

    @property
    def height(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        return max(self._height(node.left), self._height(node.right))

    def _height(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def size(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        if node is None:
            return 0

        return 1 + (self.size(node.left) if node.left else 0) + (self.size(node.right) if node.right else 0)

    def height_in_vertex(self, node: Optional[Node[T]] = None) -> int:
        if node is None:
            node = self._root
        return 1 + max(self._height(node.left), self._height(node.right))

    def find(self, value: T, node: Optional[Node[T]] = None) -> Optional[Node[T]]:
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

    def postorder(self, node: Optional[Node[T]]=None) -> Iterator[T]:
        if node is None:
            node = self._root
        if node is None:
            return

        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node.value

    def bfs(self, order_left: bool = True) -> Iterator[T]:
        current = self._root

        queue = Queue[Node[T]]([current])

        while not queue.is_empty():
            node = queue.pop()
            yield node.value
            if order_left:
                queue.push(node.left) if node.left else None
                queue.push(node.right) if node.right else None
            else:
                queue.push(node.right) if node.right else None
                queue.push(node.left) if node.left else None

    def bfs_nodes(self, order_left: bool = True) -> Iterator[Node[T]]:
        current = self._root

        queue = Queue[Node[T]]([current])

        while not queue.is_empty():
            node = queue.pop()
            yield node
            if order_left:
                queue.push(node.left) if node.left else None
                queue.push(node.right) if node.right else None
            else:
                queue.push(node.right) if node.right else None
                queue.push(node.left) if node.left else None

    def path_to(self, value: T) -> Iterator[T]:
        if self.find(value) is None:
            raise NonFindError("Can't find a path to node with value '{}' because this node is not exist".format(value))

        current = self._root

        while True:
            if current is None:
                break
            if current.value > value:
                yield current.value
                current = current.left
            elif current.value < value:
                yield current.value
                current = current.right
            else:
                yield current.value
                break

    def depth(self, value: T) -> int:
        depth = 0
        for _ in self.path_to(value):
            depth += 1
        return depth

    def to_list(self) -> List[T]:
        return list(self)

    def is_balanced(self, node: Optional[Node[T]] = None) -> bool:
        def check(n: Optional[Node[T]]) -> Tuple[int, bool]:
            if n is None:
                return 0, True
            lh, lb = check(n.left)
            rh, rb = check(n.right)
            balanced = lb and rb and abs(lh - rh) <= 1
            return 1 + max(lh, rh), balanced

        _, result = check(self._root if node is None else node)
        return result