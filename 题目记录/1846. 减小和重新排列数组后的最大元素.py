class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        cnt = (len(arr) + 1) * [0]
        for i in arr:
            if i >= len(arr) + 1:
                cnt[-1] += 1
            else:
                cnt[i - 1] += 1
        miss = 0
        for i in range(len(cnt) - 1):
            if cnt[i] > 0:
                if miss > 0 and cnt[i] >= 2:
                    miss -= cnt[i] - 1
                    miss = max(0, miss)
            else:
                miss += 1
        miss -= cnt[-1]
        if miss <= 0:
            return len(arr)
        else:
            return len(arr) - miss