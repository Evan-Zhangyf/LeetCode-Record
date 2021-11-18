# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def helper(root):
            if root == None:
                return 0, 0
            left_ans, left_sum = helper(root.left)
            right_ans, right_sum = helper(root.right)
            return left_ans + right_ans + abs(left_sum - right_sum), left_sum + right_sum + root.val
        ans, _ = helper(root)
        return ans