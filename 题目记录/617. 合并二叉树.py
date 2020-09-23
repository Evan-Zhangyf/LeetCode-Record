# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def helper(t1, t2):
            if t1 == None and t2 == None:
                return None
            if t1 and t2:
                t = TreeNode(t1.val + t2.val)
            if t1 and t2 == None:
                t = TreeNode(t1.val)
            if t1 == None and t2:
                t = TreeNode(t2.val)
            return t
        
        def merge(root, t1, t2):
            if root == None:
                return
            if t1 == None:
                t1left = None
                t1right = None
            else:
                t1left = t1.left
                t1right = t1.right
            if t2 == None:
                t2left = None
                t2right = None
            else:
                t2left = t2.left
                t2right = t2.right
            root.left = helper(t1left, t2left)
            root.right = helper(t1right, t2right)
            merge(root.left, t1left, t2left)
            merge(root.right, t1right, t2right)

        root = helper(t1, t2)
        merge(root, t1, t2)
        return root
