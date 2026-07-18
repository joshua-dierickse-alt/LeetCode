# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x, left, right):
#         self.val = x

# Node = {Val,Node,Node} | *

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(node):
            if node is None:
                res.append("*")
                return

            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        data = iter(data.split(","))

        def preorder():
            cur = next(data)

            if cur == "*":
                return None

            return TreeNode(int(cur), preorder(), preorder())
            
        return preorder()
        
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))