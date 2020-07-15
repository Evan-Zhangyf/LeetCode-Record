# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        cur1 = l1
        cur2 = l2
        ans_head = ListNode()
        ans_cur = ans_head
        while True:
            if cur1 == None or (cur2 != None and cur1.val > cur2.val):
                ans_cur.val = cur2.val
                cur2 = cur2.next
            else:
                ans_cur.val = cur1.val
                cur1 = cur1.next
            if cur1 == None and cur2 == None:
                break
            ans_cur.next = ListNode()
            ans_cur = ans_cur.next

        return ans_head