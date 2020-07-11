# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        from collections import deque
        ans = [root.val]
        q = deque()
        q.append(root)
        while len(q) != 0:
            cur = q.popleft()
            if cur.left != None:
                ans.append(cur.left.val)
                q.append(cur.left)
            if cur.right != None:
                ans.append(cur.right.val)
                q.append(cur.right)
        return ans