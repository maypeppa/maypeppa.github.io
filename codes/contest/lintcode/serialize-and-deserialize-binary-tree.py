"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        def fn(root, res):
            if root is None:
                res.append('#')
                return
            res.append(root.val)
            fn(root.left, res)
            fn(root.right, res)
        res = []
        fn(root, res)
        return res

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here

        def fn(res, idx):
            if res[idx] == '#':
                return None, idx + 1
            val = res[idx]
            left, next_idx = fn(res, idx + 1)
            right, next_idx = fn(res, next_idx)
            node = TreeNode(val)
            node.left =left
            node.right= right
            return node, next_idx

        node, _ = fn(data, 0)
        return node
