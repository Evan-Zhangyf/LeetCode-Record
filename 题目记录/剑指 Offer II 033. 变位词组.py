class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for w in strs:
            bit_map = [0] * 26
            for l in w:
                bit_map[ord(l) - ord('a')] += 1
            dic[tuple(bit_map)].append(w)
        ans = []
        for k in dic:
            ans.append(dic[k])
        return ans