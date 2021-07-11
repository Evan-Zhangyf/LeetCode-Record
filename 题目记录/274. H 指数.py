class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = [0] * (len(citations) + 1)
        for i in citations:
            if i >= len(citations):
                cnt[-1] += 1
            else:
                cnt[i] += 1
        cnt_sum = 0
        for i in range(len(citations), -1, -1):
            cnt_sum += cnt[i]
            if cnt_sum >= i:
                return i