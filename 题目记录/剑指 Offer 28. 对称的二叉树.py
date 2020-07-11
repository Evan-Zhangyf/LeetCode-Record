# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, A, B):
        if A == None and B == None:
            return True

        if A == None or B == None:
            return False

        if A.val != B.val:
            return False
        return self.helper(A.left, B.right) and self.helper(A.right, B.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.helper(root.left, root.right)