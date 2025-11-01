from typing import TypeVar, List, Iterable, Iterator

T = TypeVar('T')
def bubble_sort[T](array: Iterable[T], deep_copy: bool = True) -> Iterable[T]:

    if deep_copy:
        temp_for_sort = list(array)
    else:
        if not isinstance(array, Iterator):
            raise TypeError(f"Cannot sort non-iterable object\nexpected an iterable, got {type(array)}")
        temp_for_sort = array

    n = len(temp_for_sort)
    for i in range(n):
        for j in range(n - i - 1):
            if temp_for_sort[j] > temp_for_sort[j + 1]:
                temp_for_sort[j], temp_for_sort[j + 1] = temp_for_sort[j + 1], temp_for_sort[j]

    if deep_copy:
        # пытаемся вернуть объект того же типа, что был на входе
        orig_type = type(array)
        try:
            return orig_type(temp_for_sort)
        except TypeError:
            return temp_for_sort
    else:
        return temp_for_sort