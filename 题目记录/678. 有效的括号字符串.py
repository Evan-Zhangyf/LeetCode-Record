class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = 0
        left_max = 0
        for l in s:
            if l == "(":
                left_min += 1
                left_max += 1
            if l == "*":
                left_min = max(0, left_min - 1)
                left_max += 1
            if l == ")":
                left_max -= 1
                if left_max < 0:
                    return False
                left_min = max(left_min - 1, 0)
        return left_min == 0