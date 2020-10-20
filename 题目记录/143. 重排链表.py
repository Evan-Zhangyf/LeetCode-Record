# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        lst = []
        while head != None:
            lst.append(head)
            head = head.next
        for i in range(len(lst) // 2):
            lst[i].next = lst[-i-1]
            if lst[i+1] != lst[-i-1]:
                lst[-i-1].next = lst[i+1]
        lst[len(lst) // 2].next = None

        
            