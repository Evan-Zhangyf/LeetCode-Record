class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = {}
        for w in words:
            if dic.get(w) == None:
                dic[w] = 1
            else:
                dic[w] += 1
        string_arr = []
        for key in dic:
            string_arr.append(key)
        # 可以用堆优化，但今天我懒了，所以直接排序~
        string_arr.sort(key = lambda x : (-dic[x], x))
        return string_arr[:k]