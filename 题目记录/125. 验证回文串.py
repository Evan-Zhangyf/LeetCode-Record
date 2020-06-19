class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = []
        for ch in s:
            if ord(ch) >= 65 and ord(ch) <= 90:
                string.append(chr(ord(ch)+32))
            elif (ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 48 and ord(ch) <= 57):
                string.append(ch)
        for i in range(len(string)//2):
            if string[i] != string[len(string)-1-i]:
                return False
        return True