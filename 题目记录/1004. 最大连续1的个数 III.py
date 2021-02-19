class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        right = 0
        ans = 0
        if A[0] == 1:
            cnt = 0
        else:
            cnt = 1
        while right < len(A) - 1:
            if cnt < K:
                right += 1
                if A[right] == 0:
                    cnt += 1
            elif cnt == K:
                right += 1
                if A[right] == 0:
                    cnt += 1
                    if A[left] == 0:
                        cnt -= 1
                    left += 1
            else:
                right += 1
                if A[right] == 0:
                    cnt += 1
                if A[left] == 0:
                    cnt -= 1
                left += 1
            if cnt <= K:
                ans = max(ans, right - left + 1)
        return ans