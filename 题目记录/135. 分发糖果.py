class Solution:
    def candy(self, ratings: List[int]) -> int:
        left = [0] * len(ratings)
        right = [0] * len(ratings)
        ans = 0
        for i in range(len(ratings)):
            if i:
                if ratings[i] > ratings[i-1]:
                    left[i] = left[i-1] + 1
                else:
                    left[i] = 1 
            else:
                left[i] = 1

        for i in range(len(ratings)-1, -1, -1):
            if i == len(ratings) - 1:
                right[i] = 1
            else:
                if ratings[i] > ratings[i+1]:
                    right[i] = right[i+1] + 1
                else:
                    right[i] = 1 
            ans += max(left[i], right[i])
        return ans