# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = []
        q_path = []
        cur = root
        while cur.val != p.val:
            p_path.append(cur)
            if p.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        p_path.append(p)
        cur = root
        while cur.val != q.val:
            q_path.append(cur)
            if q.val > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        q_path.append(q)
        pos = 0
        while p_path[pos] == q_path[pos]:
            pos += 1
            if pos == min(len(q_path), len(p_path)):
                break
        return p_path[pos-1]
        
