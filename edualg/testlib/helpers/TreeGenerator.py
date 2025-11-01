import random
from typing import TypeVar, List

from edualg.structures.tree import BinarySearchTree

T = TypeVar('T')

# Создаёт BST дерево на основе мин и макс значений размера size
def random_bst[T](min_value=None, max_value=None, size=100):
    if min_value is None:
        min_value = 0
    if max_value is None:
        max_value = 1e4
    bst = BinarySearchTree[T]()

    for _ in range(size):
        value_for_fill = round(random.uniform(min_value, max_value))
        bst.insert(value_for_fill)

    return bst

# Заполняет и создаёт BST дерево на основе массива
def fill_bst(array: List[T]) -> BinarySearchTree[T]:
    bst = BinarySearchTree[T]()
    for value in array:
        bst.insert(value)
    return bst

