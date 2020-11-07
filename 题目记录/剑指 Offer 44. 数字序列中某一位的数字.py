class Solution:
    def findNthDigit(self, n: int) -> int:
        length = 1
        len_sum = 10
        while n >= len_sum:
            n = n - len_sum
            length += 1
            len_sum = 9 * (10 ** (length - 1)) * length
        if length == 1:
            num = 0
        else:
            num = 10 ** (length - 1)
        num += n // length
        return int(str(num)[n % length])