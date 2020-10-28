class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = {}
        for i in arr:
            if cnt.get(i):
                cnt[i] += 1
            else:
                cnt[i] = 1
        searched = {}
        dic = {}
        for i in arr:
            if not searched.get(i):
                searched[i] = True
                if dic.get(cnt[i]):
                    return False
                else:
                    dic[cnt[i]] = True
        return True