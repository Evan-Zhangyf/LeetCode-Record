class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        idx = {}
        for i in range(len(target)):
            idx[target[i]] = i
        arr_list = []
        for i in arr:
            if idx.get(i) != None:
                arr_list.append(idx[i])

        def lengthOfLIS(nums):
            if nums == []:
                return 0
            dp = [nums[0]]
            for i in range(1, len(nums)):
                if nums[i] > dp[-1]:
                    dp.append(nums[i])
                else:
                    left = 0
                    right = len(dp)
                    while left < right:
                        mid = left + (right - left) // 2
                        if dp[mid] < nums[i]:
                            left = mid + 1
                        else:
                            right = mid
                    dp[left] = nums[i]
            return len(dp)
        return len(target) - lengthOfLIS(arr_list)