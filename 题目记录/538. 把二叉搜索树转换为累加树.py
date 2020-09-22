# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def convert(root):
            nonlocal cur_sum
            if not root:
                return
            convert(root.right)
            cur_sum += root.val
            root.val = cur_sum
            convert(root.left)
        convert(root)
        return root