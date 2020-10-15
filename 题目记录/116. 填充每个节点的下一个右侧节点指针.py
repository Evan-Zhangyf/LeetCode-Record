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
            return root
        from collections import deque
        q = deque([root])
        while len(q) != 0:
            cur_list = []
            for i in range(len(q)):
                cur = q.popleft()
                cur_list.append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            for i in range(len(cur_list)):
                if i != len(cur_list) - 1:
                    cur_list[i].next = cur_list[i+1]
                else:
                    cur_list[i].next = None
        return root
