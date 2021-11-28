class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        ans = []
        match_cnt = 0
        dic = defaultdict(int)
        match_dic = defaultdict(int)
        for i in range(len(p)):
            match_dic[p[i]] += 1
        max_cnt = len(match_dic)
        for i in range(len(p)):
            dic[s[i]] += 1
            if match_dic[s[i]] > 0:
                if dic[s[i]] == match_dic[s[i]]:
                    match_cnt += 1
                if dic[s[i]] == match_dic[s[i]] + 1:
                    match_cnt -= 1
        if match_cnt == max_cnt:
            ans.append(0)
        for i in range(len(p), len(s)):
            dic[s[i]] += 1
            if match_dic[s[i]] > 0:
                if dic[s[i]] == match_dic[s[i]]:
                    match_cnt += 1
                if dic[s[i]] == match_dic[s[i]] + 1:
                    match_cnt -= 1
            dic[s[i-len(p)]] -= 1
            if match_dic[s[i-len(p)]] > 0:
                if dic[s[i-len(p)]] == match_dic[s[i-len(p)]]:
                    match_cnt += 1
                if dic[s[i-len(p)]] == match_dic[s[i-len(p)]] - 1:
                    match_cnt -= 1
            if match_cnt == max_cnt:
                ans.append(i - len(p) + 1)
        return ans

