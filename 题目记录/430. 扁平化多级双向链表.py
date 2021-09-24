"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def helper(head):
            if not head:
                return None
            cur = head
            while cur:
                prev = cur
                if cur.child:
                    tmp = helper(cur.child)
                    tmp.next = cur.next
                    if cur.next:
                        cur.next.prev = tmp
                    cur.next = cur.child
                    cur.child.prev = cur
                    cur.child = None
                    cur = tmp
                else:
                    cur = cur.next
            return prev
        helper(head)
        return head