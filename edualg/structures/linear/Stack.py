from typing import TypeVar, Generic, Iterator, Iterable, List

from edualg.structures.linear import DoublyLinkedList

class StackEmptyError(Exception):
    pass

T = TypeVar('T')
class Stack(Generic[T]):
    def __init__(self, array: Iterable[T] = None) -> None:
        self._stack = DoublyLinkedList[T]()
        if array:
            for item in array:
                self._stack.append(item)

    def __len__(self) -> int:
        return len(self._stack)

    def push(self, item: T) -> None:
        self._stack.append(item)

    def pop(self) -> T:
        if len(self._stack) == 0:
            raise StackEmptyError("Stack is empty")
        return self._stack.pop()

    def peek(self) -> T:
        return self._stack[-1]

    @property
    def top(self):
        if self.is_empty():
            raise StackEmptyError("Stack is empty")
        return self.peek()

    def is_empty(self) -> bool:
        return len(self) == 0

    def clear(self) -> None:
        self._stack.clear()

    def copy(self) -> 'Stack[T]':
        new_stack = Stack[T]()
        for item in self._stack:
            new_stack.push(item)
        return new_stack

    def extend(self, items: Iterable[T]) -> None:
        for item in items:
            self.push(item)

    def to_list(self) -> List[T]:
        return list(self._stack)

    def reverse(self) -> 'Stack[T]':
        reversed_stack = Stack[T]()
        for item in reversed(self._stack):
            reversed_stack.push(item)
        return reversed_stack

    def search(self, item: T) -> T:
        for item in self._stack:
            if item == item:
                return item
        return None

    @property
    def max(self) -> T:
        if len(self._stack) == 0:
            raise StackEmptyError("Stack is empty")
        max_val = self._stack[0]
        for item in self._stack:
            if item > max_val:
                max_val = item

        return max_val

    @property
    def min(self) -> T:
        if len(self._stack) == 0:
            raise StackEmptyError("Stack is empty")
        min_val = self._stack[0]
        for item in self._stack:
            if item < min_val:
                min_val = item

        return min_val

    @classmethod
    def from_iterable(cls, iterable: Iterable[T]) -> "Stack[T]":
        return cls(iterable)

    def __iter__(self) -> Iterator[T]:
        current = self._stack._tail
        while current:
            yield current.value
            current = current.prev

    def __repr__(self) -> str:
        s = 'TOP OF STACK\n'
        for item in self:
            s += f'{item}\n'
        s += "BOTTOM OF STACK"
        return s

    def __eq__(self, other: 'Stack[T]') -> bool:
        if not isinstance(other, Stack) or len(self) != len(other):
            return False

        return self.to_list() == other.to_list()

    def __bool__(self) -> bool:
        return len(self) != 0

    def __getitem__(self, index: int) -> T:
        if abs(index) > len(self):
            raise IndexError("Index of stack out of range")
        return self._stack[index]

    def __contains__(self, item: T) -> bool:
        return item in self._stack