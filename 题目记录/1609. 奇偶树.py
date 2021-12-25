# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        q = deque([root])
        level = 0
        while q:
            if level % 2:
                prev = float('inf')
            else:
                prev = 0
            # traverse current level and append nodes of next level to queue
            for _ in range(len(q)):
                cur = q.popleft()
                if level % 2:
                    if cur.val % 2 == 1 or cur.val >= prev:
                        return False
                else:
                    if cur.val % 2 == 0 or cur.val <= prev:
                        return False
                prev = cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            level += 1
        return True

