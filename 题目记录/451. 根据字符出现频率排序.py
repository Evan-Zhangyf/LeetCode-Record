class Solution:
    def frequencySort(self, s: str) -> str:
        ans = list(s)
        dic = defaultdict(int)
        for letter in s:
            dic[letter] += 1
        ans.sort(key = lambda x : (-dic[x], x))
        return "".join(ans)
        
