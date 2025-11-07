from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Iterable, List

T = TypeVar('T')

class BaseHeap(ABC, Generic[T]):
    def __init__(self, iterable: Iterable[T] = None):
        self._heap: List[T] = []
        if iterable:
            for item in iterable:
                self.insert(item)

    def __len__(self) -> int:
        return len(self._heap)

    def __iter__(self) -> Iterable[T]:
        return iter(self._heap)

    def __repr__(self) -> str:
        return f'Heap: {repr(self._heap)}'

    def size(self) -> int:
        return len(self._heap)

    def insert(self, item: T) -> None:

        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)

    def peek(self) -> T:
        return self._heap[0]

    @property
    def heap(self) -> List[T]:
        return self._heap

    @property
    def top(self) -> T:
        return self._heap[0]

    def extract(self) -> T:
        if not self._heap:
            raise IndexError('heap is empty')
            return None
        root = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._heapify_down(0)
        return root

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self._compare(self._heap[index], self._heap[parent]):
            self._heap[parent], self._heap[index] = self._heap[index], self._heap[parent]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        while True:
            extreme_idx = index
            left = 2 * extreme_idx + 1
            right = 2 * extreme_idx + 2

            if left < len(self) and self._compare(self._heap[left], self._heap[extreme_idx]):
                extreme_idx = left
            if right < len(self) and self._compare(self._heap[right], self._heap[extreme_idx]):
                extreme_idx = right

            if extreme_idx == index:
                return
            self._heap[extreme_idx], self._heap[index] = self._heap[index], self._heap[extreme_idx]
            index = extreme_idx

    def pretty_print(self):
        n = len(self._heap)
        level = 0
        next_level = 2 ** level
        for i in range(n):
            print(self._heap[i], end=" ")
            if i + 1 == next_level:
                print()
                level += 1
                next_level += 2 ** level
        print()

    def is_valid(self) -> bool:
        n = len(self)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            extreme_idx = i

            if left < n and self._compare(self._heap[left], self._heap[extreme_idx]):
                extreme_idx = left
            if right < n and self._compare(self._heap[right], self._heap[extreme_idx]):
                extreme_idx = right

            if extreme_idx != i:
                return False
        return True

    def clear(self) -> None:
        self._heap.clear()

    def merge(self, other: 'BaseHeap[T]') -> 'BaseHeap[T]':
        combined = self._heap + other._heap
        return self.build_heap(combined)

    def merge_inplace(self, other: 'BaseHeap[T]') -> None:
        self._heap += other._heap
        for i in reversed(range(len(self)// 2)):
            self._heapify_down(i)

    def replace_root(self, value: T) -> T:
        root = self._heap[0]
        self._heap[0] = value
        self._heapify_down(0)
        return root

    def copy(self) -> 'BaseHeap[T]':
        return self.build_heap(self._heap)

    def to_list_sorted(self) -> List[T]:
        copied = self.copy()
        result = []
        while copied._heap:
            result.append(copied.extract())
        return result

    @classmethod
    def build_heap(cls, array: List[T]) -> 'BaseHeap[T]':
        heap = cls()
        heap._heap = array
        for i in reversed(range(len(array) // 2)):
            heap._heapify_down(i)

        return heap

    @abstractmethod
    def _compare(self, a: T, b: T) -> bool:
        """Определяем порядок сравнения"""
        pass
