class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic = {}
        max_freq = 1
        for i in range(len(nums)):
            if dic.get(nums[i]):
                dic[nums[i]][0] += 1
                dic[nums[i]][2] = i + 1
                max_freq = max(max_freq, dic[nums[i]][0])
            else:
                dic[nums[i]] = [1, i, i + 1]
        ans = 50001
        for i in range(len(nums)):
            if dic[nums[i]][0] == max_freq:
                ans = min(ans, dic[nums[i]][2] - dic[nums[i]][1])
        return ans