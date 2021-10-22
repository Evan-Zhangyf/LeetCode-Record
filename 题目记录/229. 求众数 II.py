class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thres = len(nums) // 3 + 1
        dic = defaultdict(int)
        ans = []
        for i in nums:
            dic[i] += 1
            if dic[i] == thres:
                ans.append(i)
        return ans