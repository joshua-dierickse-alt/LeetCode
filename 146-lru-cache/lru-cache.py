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

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_front(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        return node

    def pop_back(self):
        node = self.tail.prev
        self.remove(node)
        return node

    def move_to_front(self, node: Node):
        self.remove(node)
        self.push_front(node)

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1
        self.linked_list.move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node is None:
            if len(self.cache) == self.capacity:
                del self.cache[self.linked_list.pop_back().key]
            self.cache[key] = self.linked_list.push_front(Node(key, value))
        else:
            self.linked_list.move_to_front(self.cache[key])
            self.cache[key].value = value
            