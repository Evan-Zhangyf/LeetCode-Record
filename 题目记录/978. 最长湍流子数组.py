class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp_odd = 1
        dp_even = 1
        ans = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                dp_odd = dp_even + 1
                dp_even = 1
            elif arr[i] < arr[i-1]:
                dp_even = dp_odd + 1
                dp_odd = 1
            else:
                dp_odd = 1
                dp_even = 1
            ans = max(ans, dp_odd, dp_even)
        return ans