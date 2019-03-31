"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def find_rec(self, root, k):
        if root is None:
            return None, 0
        value, left_count = self.find_rec(root.left, k)
        if value is not None:
            return value, 0
        if (left_count + 1) == k:
            return root.val, 0
        value, right_count = self.find_rec(root.right, k - (left_count + 1))
        if value is not None:
            return value, 0
        return None, (left_count + right_count + 1)

    def kthSmallest(self, root, k):
        # write your code here
        value, _ = self.find_rec(root, k)
        return value
