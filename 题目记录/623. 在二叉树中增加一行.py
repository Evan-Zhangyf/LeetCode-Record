# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            ret = TreeNode(val, root)
            return ret
        from collections import deque
        q = deque([root])
        cur_depth = 1
        while cur_depth < depth - 1:
            for i in range(len(q)):
                tmp = q.popleft()
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            cur_depth += 1
        for i in range(len(q)):
            q[i].left = TreeNode(val, q[i].left, None)
            q[i].right = TreeNode(val, None, q[i].right)
        return root