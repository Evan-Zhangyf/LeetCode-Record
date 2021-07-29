class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        cur = 1
        d = 1
        while label > cur:
            cur = (cur + 1) * 2 - 1
            d += 1
        ans = [0] * d
        ans[-1] = label
        ans[0] = 1
        if d % 2 == 0:
            # inversed
            inverse = 1
            pos = 2 ** d - label
        else:
            # not inversed
            inverse = -1
            pos = label - 2 ** (d - 1) + 1
        for i in range(len(ans) - 2):
            d -= 1
            pos = (pos + 1) // 2
            inverse *= -1
            if inverse == -1:
                ans[len(ans) - i - 2] = 2 ** (d - 1) - 1 + pos
            else:
                ans[len(ans) - i - 2] = 2 ** d - pos
        return ans