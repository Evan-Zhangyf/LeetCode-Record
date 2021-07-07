class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = defaultdict(int)
        max_val = 2 * max(deliciousness)
        ans = 0
        for dish in deliciousness:
            cur = 1
            while cur <= max_val:
                ans += dic[cur - dish]
                cur *= 2
            dic[dish] += 1
        return ans % (10 ** 9 + 7)
            