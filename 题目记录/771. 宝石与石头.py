class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_dict = {}
        for i in J:
            if J_dict.get(i) == None:
                J_dict[i] = 0
        for i in S:
            if J_dict.get(i) != None:
                J_dict[i] += 1
        ans = 0
        for i in J:
            ans += J_dict[i]
        return ans