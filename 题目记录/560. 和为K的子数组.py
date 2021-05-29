class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        cur = 0
        ans = 0
        for n in nums:
            cur += n
            if dic.get(cur - k) != None:
                ans += dic[cur - k]
            if cur == k:
                ans += 1
            if dic.get(cur) != None:
                dic[cur] += 1
            else:
                dic[cur] = 1
        return ans