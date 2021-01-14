class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        cur_num = 0
        ans = []
        for i in A:
            cur_num = cur_num * 2 + i
            if cur_num % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans