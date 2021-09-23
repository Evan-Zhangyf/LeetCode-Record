class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        ans = list(palindrome)
        for i in range(len(ans)):
            if ans[i] > 'a' and 2 * i + 1 != len(ans):
                ans[i] = 'a'
                return "".join(ans)
        ans[-1] = 'b'
        return "".join(ans)
        