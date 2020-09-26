# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        def dfs(root, path, path_sum):
            if path_sum == sum and root.left == None and root.right == None:
                ans.append(path)
                return
            if root.left:
                dfs(root.left, path + [root.left.val], path_sum + root.left.val)
            if root.right:
                dfs(root.right, path + [root.right.val], path_sum + root.right.val)
        dfs(root, [root.val], root.val)
        return ans