# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        big = max(p.val, q.val)
        small = min(p.val, q.val)
        def helper(root, big, small):
            if root.val <= big and root.val >= small:
                return root
            if root.val > big:
                return helper(root.left, big, small)
            if root.val < small:
                return helper(root.right, big, small)
        return helper(root, big, small)