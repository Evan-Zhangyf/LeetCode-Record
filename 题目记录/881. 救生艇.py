class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        from collections import deque
        people.sort()
        q = deque(people)
        ans = 0
        while len(q) > 0:
            if len(q) == 1:
                ans += 1
                q.pop()
            else:
                if q[0] + q[-1] <= limit:
                    q.pop()
                    q.popleft()
                    ans += 1
                else:
                    q.pop()
                    ans += 1
        return ans