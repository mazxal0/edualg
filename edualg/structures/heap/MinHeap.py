from typing import TypeVar, Iterable

from edualg.structures.heap.BaseHeap import BaseHeap

T = TypeVar('T')
class MinHeap(BaseHeap[T]):
    def __init__(self, items: Iterable[T] = None):
        super().__init__(items)

    def _compare(self, a: T, b: T) -> bool:
        return a < b