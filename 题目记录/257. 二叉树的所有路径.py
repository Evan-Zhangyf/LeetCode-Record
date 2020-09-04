# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # 特判
        if root == None:
            return []
        ans = []
        def dfs(path, root):
            if root.left == None and root.right == None:
                ans.append(path)
                return
            if root.left != None:
                dfs(path + "->" + str(root.left.val), root.left)
            if root.right != None:
                dfs(path + "->" + str(root.right.val), root.right)
        dfs(str(root.val), root)
        return ans