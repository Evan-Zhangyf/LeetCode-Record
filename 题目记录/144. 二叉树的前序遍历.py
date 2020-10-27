# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        node_stack = []
        cur = root
        while cur != None or len(node_stack)>0:
            while cur != None:
                node_stack.append(cur)
                node_list.append(cur.val)
                cur = cur.left
            cur = node_stack.pop()
            cur = cur.right
        return node_list