class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        dic = defaultdict(int)
        cnt = 0
        ans = []
        for i in range(len(changed)):
            if dic[changed[i]] > 0:
                dic[changed[i]] -= 1
                cnt += 1
            else:
                dic[2*changed[i]] += 1
                ans.append(changed[i])
        if cnt == len(ans):
            return ans
        else:
            return []