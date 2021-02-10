class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dic_s2 = [0] * 26
        dic_s1 = [0] * 26
        left = 0
        right = len(s1) - 1
        for i in range(len(s1)):
            dic_s1[ord(s1[i]) - ord("a")] += 1
            dic_s2[ord(s2[i]) - ord("a")] += 1
        while True:
            if dic_s1 == dic_s2:
                return True
            dic_s2[ord(s2[left]) - ord("a")] -= 1
            if right == len(s2) - 1:
                return False
            left += 1
            right += 1
            dic_s2[ord(s2[right]) - ord("a")] += 1