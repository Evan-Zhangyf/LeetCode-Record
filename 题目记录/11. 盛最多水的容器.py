class Solution:
    def maxArea(self, height):
        #双指针，看了答案
        if len(height)==1 or height==[]:
            return 0
        left = 0
        right = len(height) - 1
        max_area = 0
        while left != right:
            tmp = (right - left) * min(height[left], height[right])
            max_area = max(tmp, max_area)
            if height[left] >= height[right]:
                right = right - 1
            else:
                left = left + 1
        return max_area