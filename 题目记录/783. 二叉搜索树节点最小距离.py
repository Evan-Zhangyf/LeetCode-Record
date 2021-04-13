# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(root):
            if root:
                dfs(root.left)
                tree_array.append(root.val)
                dfs(root.right)
        tree_array = []
        dfs(root)
        ans = 1e5
        for i in range(1, len(tree_array)):
            ans = min(tree_array[i] - tree_array[i-1], ans)
        return ans