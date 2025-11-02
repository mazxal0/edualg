from edualg.algorithms.sorts import bubble_sort
from edualg.structures.tree import BinarySearchTree


def main():
    bst = BinarySearchTree[int]([1, 2, -1])
    bst.delete(1)
    for v in bst.bfs():
        print(v)

if __name__ == '__main__':
    main()