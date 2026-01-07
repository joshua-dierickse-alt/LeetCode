# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def nodesToSum(node):
    if not node:
        return 0
    node.val = nodesToSum(node.left) + node.val + nodesToSum(node.right)
    return node.val

def leftSplit(node):
    return (s - node.left.val) * node.left.val

def rightSplit(node):
    return (s - node.right.val) * node.right.val

def getMaxSplit(node):
    return max(max(leftSplit(node), getMaxSplit(node.left)) if node.left else 0,
               max(rightSplit(node), getMaxSplit(node.right)) if node.right else 0)

s = None

class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        global s

        nodesToSum(root)
        s = root.val
        return getMaxSplit(root) % (10**9+7)
        