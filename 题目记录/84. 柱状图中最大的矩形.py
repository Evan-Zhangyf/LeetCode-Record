class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [0] * len(heights)
        right = [0] * len(heights)
        s = []
        for i in range(len(heights)):
            if s == [] or heights[i] >= heights[s[-1]]:
                s.append(i)
            else:
                while s and heights[s[-1]] > heights[i]:
                    right[s[-1]] = i
                    s.pop()
                s.append(i)
        while s:
            right[s[-1]] = len(heights)
            s.pop()
        
        for i in range(len(heights) - 1, -1, -1):
            if s == [] or heights[i] >= heights[s[-1]]:
                s.append(i)
            else:
                while s and heights[s[-1]] > heights[i]:
                    left[s[-1]] = i
                    s.pop()
                s.append(i)
        while s:
            left[s[-1]] = -1
            s.pop()
        
        ans = 0
        for i in range(len(heights)):
            ans = max(ans, heights[i] * (right[i] - left[i] - 1))
        return ans