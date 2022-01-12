class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(int)
        ans = 0
        for w in words:
            dic[w] += 1
        center_flag = False
        for w in list(dic.keys()):
            if dic[w] > 0:
                if w[1] != w[0]:
                    if dic[w[1]+w[0]] > 0:
                        tmp = min(dic[w], dic[w[1]+w[0]])
                        dic[w] -= tmp
                        dic[w[1]+w[0]] -= tmp
                        ans += 4 * tmp
                else:
                    if dic[w] % 2 == 0:
                        ans += 2 * dic[w]
                        dic[w] = 0
                    else:
                        if center_flag == False:
                            center_flag = True
                            ans += dic[w] * 2
                            dic[w] = 0
                        else:
                            ans += (dic[w] - 1) * 2
                            dic[w] = 1

        return ans

