from typing import Iterable, TypeVar

from edualg.structures.heap.BaseHeap import BaseHeap

T = TypeVar('T')
class MaxHeap(BaseHeap):
    def __init__(self, items: Iterable[T] = None):
        super().__init__(items)

    def _compare(self, a: T, b: T) -> bool:
        return a > b