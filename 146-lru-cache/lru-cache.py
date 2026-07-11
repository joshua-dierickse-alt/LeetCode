from dataclasses import dataclass

@dataclass
class Node:
    key: int
    value: int
    left: Node
    right: Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_head(self, key: int, head: int):
        self.head = Node(key=key, value=head, left=None, right=self.head)
        if self.head.right:
            self.head.right.left = self.head
        if self.tail == None:
            self.tail = self.head

    def delete_tail(self):
        self.delete_node(self.tail)

    def delete_node(self, node: Node):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = self.head.right
            self.head.left = None
        elif self.tail == node:
            self.tail = self.tail.left
            self.tail.right = None
        else:
            if node.left:
                node.left.right = node.right
            if node.right:
                node.right.left = node.left

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.cache = {}

    def update_value(self, key, value):
        self.linked_list.delete_node(self.cache[key])
        self.linked_list.append_head(key, value)
        self.cache[key] = self.linked_list.head

    def delete_tail(self):
        del self.cache[self.linked_list.tail.key]
        self.linked_list.delete_tail()

    def append_head(self, key, value):
        self.linked_list.append_head(key, value)
        self.cache[key] = self.linked_list.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.update_value(key, self.cache[key].value)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.update_value(key, value)
        else:
            if len(self.cache) == self.capacity:
                self.delete_tail()
            self.append_head(key, value)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)