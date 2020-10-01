class Solution:
    def permutation(self, s: str) -> List[str]:
        s = list(s)
        s.sort()
        s_cnt = {}
        ans = []
        for i in s:
            if not s_cnt.get(i):
                s_cnt[i] = 1
            else:
                s_cnt[i] += 1
        def back(ss):
            if len(ss) == len(s):
                ans.append(ss)
                return
            for i in range(len(s)):
                if s_cnt[s[i]] > 0 and (i == 0 or s[i] != s[i-1]):
                    s_cnt[s[i]] -= 1
                    back(ss + s[i])
                    s_cnt[s[i]] += 1
        back("")
        return ans