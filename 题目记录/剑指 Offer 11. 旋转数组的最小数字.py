class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while right - left > 1:
            mid = (left + right) / 2
            mid = int(mid)
            if numbers[mid] > numbers[right]:
                left = mid
            elif numbers[mid] < numbers[left]:
                right = mid
            else:
                right -= 1
        return min(numbers[left: right+1])