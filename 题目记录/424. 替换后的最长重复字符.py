class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0 or len(s) == 1:
            return len(s)
        left = 0
        right = 0
        cnt = [0] * 26
        cnt[ord(s[0])-ord("A")] = 1
        max_letter = s[0]
        while True:
            right += 1
            cnt[ord(s[right])-ord("A")] += 1
            if cnt[ord(s[right])-ord("A")] > cnt[ord(max_letter)-ord("A")]:
                max_letter = s[right]
            if right - left - cnt[ord(max_letter)-ord("A")] + 1 > k:
                cnt[ord(s[left])-ord("A")] -= 1
                max_letter = chr(cnt.index(max(cnt)) + ord("A"))
                left += 1
            if right == len(s) - 1:
                break
        return right - left + 1