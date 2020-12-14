class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def convert(word):
            ret = [0] * 26
            for i in word:
                ret[ord(i) - 97] += 1
            return str(ret)
        dic = {}
        for i in strs:
            tmp = convert(i)
            if dic.get(tmp):
                dic[tmp].append(i)
            else:
                dic[tmp] = [False, i]
        ans = []
        for i in strs:
            tmp = convert(i)
            if not dic[tmp][0]:
                ans.append(dic[tmp][1:])
                dic[tmp][0] = True
        return ans