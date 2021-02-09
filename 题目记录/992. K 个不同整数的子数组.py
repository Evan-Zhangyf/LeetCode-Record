class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def subarraysWithMaxKDistinct(A, K):
            left = 0
            right = 0
            diff_num = 1
            dic = [0] * len(A)
            dic[A[0] - 1] = 1
            ret = 0
            while left <= len(A) - 1:
                if right == len(A) - 1 or diff_num > K:
                    if diff_num > K:
                        ret += right - left
                    else:
                        ret += right - left + 1
                    if dic[A[left] - 1] == 1:
                        diff_num -= 1
                    dic[A[left] - 1] -= 1
                    left += 1
                else:
                    right += 1
                    if dic[A[right] - 1] == 0:
                        diff_num += 1
                    dic[A[right] - 1] += 1

            if diff_num > K:
                ret += right - left
            else:
                ret += right - left + 1
            return ret
        return subarraysWithMaxKDistinct(A, K) - subarraysWithMaxKDistinct(A, K - 1)