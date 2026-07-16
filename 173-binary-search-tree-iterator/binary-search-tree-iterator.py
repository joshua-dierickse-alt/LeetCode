import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def in_order(node):
    if node:
        yield from in_order(node.left)
        yield node.val
        yield from in_order(node.right)

class BSTIterator:
    def safe_next(self):
        try:
            return next(self.iter)
        except:
            return math.inf

    def __init__(self, root: Optional[TreeNode]):
        self.iter = in_order(root)
        self.next_val = self.safe_next()

    def next(self) -> int:
        temp = self.next_val
        self.next_val = self.safe_next()
        return temp

    def hasNext(self) -> bool:
        return math.inf != self.next_val
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()