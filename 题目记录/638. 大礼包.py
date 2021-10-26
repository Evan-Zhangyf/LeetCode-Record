class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        dic = {}
        s = []
        n = len(price)
        for offer in special:
            tmp = 0
            for i in range(n):
                tmp += offer[i] * price[i]
            if tmp > offer[n]:
                s.append(offer)
        
        def helper(need):
            if dic.get(need):
                return dic[need]
            ret = float('inf')
            for offer in s:
                tmp = []
                for i in range(n):
                    if need[i] >= offer[i]:
                        tmp.append(need[i] - offer[i])
                    else:
                        break
                if len(tmp) == n:
                    ret = min(ret, helper(tuple(tmp)) + offer[n])
            if ret == float('inf'):
                ret = 0
                for i in range(n):
                    ret += need[i] * price[i]
            return ret
        
        return helper(tuple(needs))
