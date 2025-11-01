from typing import TypeVar, Generic, Optional

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value):
        self.next: Optional[T] = None
        self.value: T = value

    def __repr__(self):
        return f'Node({self.value})'


class LinkedList(Generic[T]):
    def __init__(self, array=None):
        self.head: Optional[T] = None
        if array:
            for value in array:
                self.append(value)


    def append(self, value: T) -> None:
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def delete(self, value: T) -> Optional[T]:
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                    return current
                previous.next = current.next
                return current
            previous = current
            current = current.next
        return None

    def display(self) -> None:
        print("START THE LINKED LIST")
        current = self.head
        while current:
            print(current.value)
            current = current.next
        print("END THE LINKED LIST")

    def find(self, value) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return " -> ".join(str(v) for v in self) + " -> None"

    def __len__(self):
        return sum(1 for _ in self)

    def reverse(self):
        return reverse_linked_list(self)

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    next_node = linked_list.head.next
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    linked_list.head = prev
    return linked_list