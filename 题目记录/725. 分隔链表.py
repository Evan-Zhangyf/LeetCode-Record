# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        length = 0
        cur = head
        while cur:
            cur = cur.next
            length += 1
        long_cnt = length % k
        list_len = length // k
        ans = []
        cur = head
        for i in range(k):
            tmp = cur
            cnt = list_len
            if i < long_cnt:
                cnt = list_len + 1
            if cnt > 0:
                for j in range(cnt - 1):
                    tmp = tmp.next
                ans.append(cur)
                cur = tmp.next
                tmp.next = None
            else:
                ans.append(None)
        return ans