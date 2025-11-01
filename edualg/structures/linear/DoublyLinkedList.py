from typing import TypeVar, Generic, Optional, Iterator, List

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T, prev: Optional[T] = None, next_node: Optional[T] = None) -> None:
        self.value = value
        self.next = next_node
        self.prev = prev

    def __repr__(self) -> T:
        return f'Node({self.value})'


class DoublyLinkedList(Generic[T]):
    def __init__(self, array: Optional[List[T]]=None) -> None:
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None
        self._length: int = 0

        if array:
            self._length = len(array)
            for value in array:
                self.append(value)

    def append(self, value: T) -> None:
        new_node = Node(value, prev=self._tail)
        if self._tail:
            self._tail.next = new_node
        else:
            self._head = new_node
        self._tail = new_node
        self._length += 1

    def prepend(self, value: T) -> None:
        new_node = Node(value, next_node=self._head)
        if self._head:
            self._head.prev = new_node
        else:
            self._tail = new_node
        self._head = new_node
        self._length += 1

    def pop(self) -> T:
        if self._tail is None:
            raise IndexError('pop from an empty DoublyLinkedList')

        value = self._tail.value
        self._tail = self._tail.prev

        if self._tail:
            self._tail.next = None
        else:
            self._head = None
        self._length -= 1
        return value

    def pop_left(self) -> T:
        if self._head is None:
            raise IndexError('pop from an empty DoublyLinkedList')

        value = self._head.value
        self._head = self._head.next

        if self._head:
            self._head.prev = None
        else:
            self._tail = None

        self._length -= 1
        return value

    def clear(self):
        self._head = self._tail = None
        self._length = 0

    def find(self, value: T) -> Optional[T]:
        if self._head is None:
            return None

        current = self._head
        while current:
            if current.value == value:
                return current.value
            current = current.next

        return None

    def delete(self, value: T) -> None:
        if self._head is None:
            raise IndexError("Deleting from an empty DoublyLinkedList")

        current = self._head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self._head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self._tail = current.prev

                self._length -= 1
                return
            current = current.next

    def insert_after(self, target: T, value: T) -> None:
        if self._head is None:
            raise IndexError("Inserting from an empty DoublyLinkedList")
        current = self._head
        new_node = Node(value)
        while current:
            if current.value == target:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self._tail = new_node
                current.next = new_node
                self._length += 1
                return
            current = current.next

    def insert_before(self, target: T, value: T) -> None:
        if len(self) == 0:
            raise IndexError("Inserting from an empty DoublyLinkedList")
        current = self._head
        new_node = Node(value)
        while current:
            if current.value == target:
                new_node.next = current
                new_node.prev = current.prev
                if current.prev:
                    current.prev.next = new_node
                else:
                    self._head = new_node
                current.prev = new_node
                self._length += 1
                return
            current = current.next

    def to_list(self) -> List[T]:
        return list(self)

    def reverse(self):
        current = self._head
        prev = None
        self._tail = self._head

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node

        self._head = prev

    def info(self):
        return f'DoublyLinkedList: {self.to_list()} \nLength: {self._length}\n__head: {self._head}\n_tail: {self._tail}'

    def copy(self) -> "DoublyLinkedList[T]":
        new_list = DoublyLinkedList[T]()
        for value in self:
            new_list.append(value)
        return new_list

    def extend(self, iterable: List[T]) -> "DoublyLinkedList[T]":
        for v in iterable:
            self.append(v)
        return self

    def insert(self, index: int, value: T) -> None:
        if not isinstance(index, int):
            raise TypeError('Insert index must be an integer')
        if index < 0 or index >= self._length:
            raise IndexError('Insert index out of range')

        if index == 0:
            self.prepend(value)
            return
        elif index == self._length:
            self.append(value)
            return

        current = self._head
        count = 0
        while current:
            if count == index:
                new_node = Node(value)
                prev = current.prev
                new_node.prev = prev
                new_node.next = current
                current.prev = new_node
                if prev is not None:
                    prev.next = new_node

                self._length += 1
                return
            current = current.next
            count += 1

    def peek_left(self) -> T:
        if self._head is None:
            raise IndexError('Peek from an empty DoublyLinkedList')
        return self._head.value

    def merge(self, other: "DoublyLinkedList[T]") -> None:
        if len(self) == 0:
            raise IndexError("Merging from an empty DoublyLinkedList")
        if len(other) == 0:
            return
        self._tail.next = other._head
        other._head.prev = self._tail
        self._length += other._length
        self._tail = other._tail

    def remove_duplicates(self) -> None:
        # TODO
        pass

    def sort(self) -> None:
        # TODO
        pass

    def __iter__(self) -> Iterator[T]:
        current = self._head
        while current:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._length

    def __repr__(self) -> str:
        return " <-> ".join(str(v) for v in self)

    def __getitem__(self, index: int) -> T:
        if self._head is None:
            raise IndexError("Setting from an empty DoublyLinkedList")
        if (index >= 0 and index >= len(self)) or (index < 0 and index < -len(self)):
            raise IndexError("Index out of range")
        if index >= 0:
            count = 0
            current = self._head
            while current:
                if count == index:
                    return current.value
                current = current.next
                count += 1
        elif index < 0:
            count = -1
            current = self._tail
            while current:
                if count == index:
                    return current.value
                current = current.prev
                count -= 1

        raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: T) -> None:
        if self._head is None:
            raise IndexError("Setting from an empty DoublyLinkedList")
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current: Node[T] = self._head
        count: int = 0
        while current:
            if count == index:
                current.value = value
            current = current.next
            count += 1

    def __reversed__(self):
        current = self._tail
        while current:
            yield current.value
            current = current.prev

    def __contains__(self, value: T) -> bool:
        return self.find(value) is not None

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DoublyLinkedList):
            return False
        return list(self) == list(other)

    def __bool__(self) -> bool:
        return self._length > 0

    def __add__(self, other):
        return self.extend(other)

    def __radd__(self, other):
        return other.extend(self)

    def __iadd__(self, other):
        return self.extend(other)