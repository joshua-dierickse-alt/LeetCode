import heapq

class Node:
    def __init__(self, left, right, height, width):
        self.left = left
        self.right = right
        self.height = height
        self.width = width
        self.deleted = False

    def __eq__(self, other):
        return self.height == other.height

    def __lt__(self, other):
        return self.height * -1 < other.height * -1

def del_right_node(node):
    node.width += node.right.width
    node.height = node.right.height
    node.right.deleted = True
    node.right = node.right.right
    if node.right:
        node.right.left = node

def del_left_node(node):
    node.width += node.left.width
    node.height = node.left.height
    node.left.deleted = True
    node.left = node.left.left
    if node.left:
        node.left.right = node

def print_ll(node):
    while node.left:
        node = node.left

    print("---")

    while node:
        print("height: ", node.height, ", width", node.width)
        node = node.right

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ll = None
        heap = []

        m = 0

        for height in heights:
            m = max(m, height)
            prev = ll
            ll = Node(ll, None, height, 1)
            if prev:
                prev.right = ll
            heapq.heappush(heap, ll)

        while heap:
            node = heapq.heappop(heap)
            if node.deleted:
                continue

            if node.left and node.right:
                if node.left.height < node.right.height:
                    del_right_node(node)
                else:
                    del_left_node(node)
            elif node.left:
                del_left_node(node)
            elif node.right:
                del_right_node(node)
            else:
                continue

            heapq.heappush(heap, node)

            m = max(m, node.height * node.width)

        return m
            