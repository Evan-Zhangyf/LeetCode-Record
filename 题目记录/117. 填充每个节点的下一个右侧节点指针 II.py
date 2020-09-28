"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        from collections import deque
        q = deque([root])
        while len(q) != 0:
            length = len(q)
            for i in range(length):
                cur = q.popleft()
                if i != length - 1:
                    cur.next = q[0]
                else:
                    cur.next = None
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return root