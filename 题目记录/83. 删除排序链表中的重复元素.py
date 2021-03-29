# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        pre_node = None
        while cur:
            if pre_node and cur.val == pre_node.val:
                pre_node.next = cur.next
                del cur
                cur = pre_node.next
            else:
                pre_node = cur
                cur = cur.next
        return head