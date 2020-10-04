# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(0)
        cur = new_head
        flag = 0
        while 1:
            if l1 != None:
                cur.val += l1.val
            if l2 != None:
                cur.val += l2.val
            cur.val += flag
            flag = int(cur.val/10)
            cur.val = cur.val%10
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            if l1 != None or l2 != None:
                cur.next = ListNode(0)
                cur = cur.next
            else:
                if flag == 0:
                    return new_head
                else:
                    cur.next = ListNode(1)
                    return new_head