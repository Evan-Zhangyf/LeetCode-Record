class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = []
        while K != 0:
            B.append(K % 10)
            K //= 10
        B.reverse()
        ans = [0] * (max(len(A), len(B)) + 1)
        flag = 0
        for i in range(1, max(len(A), len(B))+1):
            if len(A) >= i:
                a = A[-i]
            else:
                a = 0
            if len(B) >= i:
                b = B[-i]
            else:
                b = 0
            tmp = a + b + flag
            flag = 0
            if tmp >= 10:
                flag = 1
                tmp = tmp % 10
            ans[-i] = tmp
        if flag == 1:
            ans[0] = 1
            return ans
        else:
            return ans[1:]