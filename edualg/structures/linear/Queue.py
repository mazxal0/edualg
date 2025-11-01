from typing import TypeVar, Generic

from edualg.structures.linear import DoublyLinkedList


class Empty(Exception):
    pass

T = TypeVar('T')
class Queue(Generic[T]):
    def __init__(self):
        self._queue = DoublyLinkedList[T]()

    def __len__(self):
        return len(self._queue)

    def push(self, item: T):
        self._queue.append(item)

    def pop(self) -> T:
        return self._queue.pop_left()

    def peek(self) -> T:
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._queue.peek_left()

    def top(self) -> T:
        return self.peek()

    def is_empty(self):
        return len(self._queue) == 0

    def __getitem__(self, index: int):
        if abs(index) > len(self._queue):
            raise IndexError("Index of queue is out of range")
        return self._queue[index]