class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        idx = []
        for i in range(len(s)):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                idx.append(i)
        
        for i in range(len(idx) // 2):
            s[idx[i]], s[idx[-i-1]] = s[idx[-i-1]], s[idx[i]]
        return "".join(s)