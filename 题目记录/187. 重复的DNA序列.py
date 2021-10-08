class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        ans = []
        dic = defaultdict(int)
        for i in range(len(s) - 9):
            tmp = s[i: i+10]
            if dic[tmp] == 0:
                dic[tmp] = 1
            elif dic[tmp] == 1:
                ans.append(tmp)
                dic[tmp] += 1
        return ans