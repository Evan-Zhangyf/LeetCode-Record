# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        inorder_pos = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:inorder_pos], postorder[:inorder_pos])
        root.right = self.buildTree(inorder[inorder_pos+1:], postorder[inorder_pos:-1])
        return root