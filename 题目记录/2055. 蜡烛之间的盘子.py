class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = defaultdict(int)
        i = 0
        while s[i] != '|' and i < len(s):
            i += 1
        cur = 0
        candle_cnt = 0
        while i < len(s):
            if s[i] == '*':
                cur += 1
            else:
                candle_cnt += cur
                cur = 0
                prefix_sum[i] = candle_cnt
            i += 1
        left = [-1] * len(s)
        right = [-1] * len(s)
        cur = -1
        for i in range(len(s)):
            if s[i] == '|':
                cur = i
            left[i] = cur
        cur = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                cur = i
            right[i] = cur
        ans = []
        for q in queries:
            if right[q[0]] > q[1] or left[q[1]] < q[0]:
                ans.append(0)
            else:
                ans.append(prefix_sum[left[q[1]]] - prefix_sum[right[q[0]]])
        return ans

