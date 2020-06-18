# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder == []:
            return None
        root_val = preorder[0]
        in_index = inorder.index(root_val)
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:in_index+1], inorder[0:in_index])
        root.right = self.buildTree(preorder[in_index+1:], inorder[in_index+1:])
        return root