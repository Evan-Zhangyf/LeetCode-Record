class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        for i in range(len(words)):
            w = list(words[i])
            w.reverse()
            words[i] = "".join(w)

        return " ".join(words)