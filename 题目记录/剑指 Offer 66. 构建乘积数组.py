class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        # dp构建i左右两边的累积乘法的结果值
        dp_left = [1] * len(a)
        dp_right = [1] * len(a)
        for i in range(1, len(a)):
            dp_left[i] = a[i - 1] * dp_left[i - 1]
        for i in range(len(a) - 2, -1, -1):
            dp_right[i] = a[i + 1] * dp_right[i + 1]
        b = []
        for i in range(len(a)):
            b.append(dp_left[i] * dp_right[i])
        return b