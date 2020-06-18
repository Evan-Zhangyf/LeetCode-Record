# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归实现
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            return left.val == right.val and helper(left.left, right.right) and helper(left.right, right.left)
        if root == None:
            return True
        return helper(root.left, root.right)