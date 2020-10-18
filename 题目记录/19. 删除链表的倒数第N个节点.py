# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        next_n = head
        cur = head
        for i in range(n):
            next_n = next_n.next
        if not next_n:
            return head.next
        while next_n:
            next_n = next_n.next
            before_cur = cur
            cur = cur.next
        before_cur.next = cur.next
        return head