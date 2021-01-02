class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q = deque([(nums[0], 0)])
        ans = []
        for i in range(1, k-1):
            while len(q) != 0 and nums[i] >= q[-1][0]:
                q.pop()
            q.append((nums[i], i))
        
        for i in range(k-1, len(nums)):
            while len(q) != 0 and nums[i] >= q[-1][0]:
                q.pop()
            while len(q) != 0 and q[0][1] <= i - k:
                q.popleft()
            q.append((nums[i], i))
            ans.append(q[0][0])
        return ans
