# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        sorted_tree = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            sorted_tree.append(root.val)
            inorder(root.right)
        inorder(root)
        ans = 10000000
        for i in range(1, len(sorted_tree)):
            ans = min(ans, sorted_tree[i] - sorted_tree[i-1])
        return ans