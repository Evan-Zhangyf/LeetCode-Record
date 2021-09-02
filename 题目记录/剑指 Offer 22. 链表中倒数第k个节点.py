# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        fast = head
        for i in range(k - 1):
            fast = fast.next
            if fast == None:
                return None
        slow = head
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        return slow