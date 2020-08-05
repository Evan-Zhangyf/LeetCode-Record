# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.dp = {}

    def rob(self, root: TreeNode) -> int:
        if root == None:
            return 0
        # 不打劫root
        not_rob_root = self.dp_rob(root.left) + self.dp_rob(root.right)
        # 打劫root
        rob_root = root.val
        if root.left != None:
            rob_root += self.dp_rob(root.left.left) + self.dp_rob(root.left.right)
        if root.right != None:
            rob_root += self.dp_rob(root.right.left) + self.dp_rob(root.right.right)
        self.dp[root] = max(not_rob_root, rob_root)
        return self.dp[root]
    
    def dp_rob(self, root):
        if self.dp.get(root):
            return self.dp[root]
        else:
            return self.rob(root)