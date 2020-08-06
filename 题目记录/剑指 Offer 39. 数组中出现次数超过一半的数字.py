class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            if hashmap.get(i):
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] > len(nums) // 2:
                return i