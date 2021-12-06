class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        end = len(s)
        cnt = 0
        for i in range(len(s)):
            if s[i] == ' ':
                cnt += 1
                if cnt == k:
                    end = i
        return s[: end]
