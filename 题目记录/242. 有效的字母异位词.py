class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = [0] * 26
        for letter in s:
            dic[ord(letter) - 97] += 1
        for letter in t:
            dic[ord(letter) - 97] -= 1
        for i in dic:
            if i != 0:
                return False
        return True