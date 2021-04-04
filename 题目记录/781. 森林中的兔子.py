class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        import math
        cnt_dic = {}
        for i in answers:
            if cnt_dic.get(i):
                cnt_dic[i] += 1
            else:
                cnt_dic[i] = 1
        
        ans = 0
        for num, v in cnt_dic.items():
            ans += math.ceil(v / (num + 1)) * (num + 1)
        return ans