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

        def recursive(node):
            if node is None:
                res.append("*")
                return

            res.append(str(node.val))
            res.append(",")
            recursive(node.left)
            res.append(",")
            recursive(node.right)

        recursive(root)
        res = "".join(res)
        return res
        
    # {1,{2,*,*},{3,{4,*,*},{5,*,*}}}

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        i = 0

        def recursive():
            nonlocal i

            if data[i] == "*":
                i += 1
                return None

            num = []
            while data[i] != ",":
                num.append(data[i])
                i += 1
            num = int("".join(num))

            i += 1
            left = recursive()
            i += 1
            right = recursive()
            return TreeNode(num, left, right)
            
        return recursive()
        
        


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))