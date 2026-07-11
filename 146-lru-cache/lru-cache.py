class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node

    def delete_tail(self):
        prev = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        return prev

    def move_to_front(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_head(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.linked_list.move_to_front(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.linked_list.move_to_front(self.cache[key])
            self.cache[key].value = value
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.linked_list.delete_tail().key]
            self.cache[key] = self.linked_list.add_head(Node(key, value))