class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = []
        flag = 0
        for i in range(len(s)):
            tmp = abs(ord(s[i]) - ord(t[i]))
            cost.append(abs(ord(s[i]) - ord(t[i])))
            if tmp <= maxCost:
                flag = 1
        if flag == 0:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        cur_cost = cost[0]
        while True:
            right += 1
            cur_cost += cost[right]
            if cur_cost > maxCost:
                cur_cost -= cost[left]
                left += 1
            if right == len(s) - 1:
                break
        return right - left + 1