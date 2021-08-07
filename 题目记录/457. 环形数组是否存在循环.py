class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def next(cur):
            return (cur + nums[cur]) % len(nums)
        visited = [False] * len(nums)
        for i in range(len(nums)):
            if visited[i] == False:
                slow = i
                fast = next(slow)
                while visited[slow] == False and nums[fast] * nums[slow] > 0 and nums[next(fast)] * nums[slow] > 0:
                    slow = next(slow)
                    fast = next(next(fast))
                    if fast == slow:
                        if slow == next(slow):
                            break
                        else:
                            return True
                prev = i
                cur = i
                while nums[prev] * nums[cur] > 0 and visited[cur] == False:
                    visited[cur] = True
                    prev = cur
                    cur = next(cur)
        return False

                    