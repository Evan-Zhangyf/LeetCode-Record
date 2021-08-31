class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for p in bookings:
            diff[p[0] - 1] += p[2]
            diff[p[1]] -= p[2]
        ans = []
        ans.append(diff[0])
        for i in range(1, len(diff) - 1):
            ans.append(ans[-1] + diff[i])
        return ans
