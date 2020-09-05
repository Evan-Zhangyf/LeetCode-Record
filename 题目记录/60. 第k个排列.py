class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 回溯法，写的很琐碎
        cur = 0
        ans = ""
        def generate_list(num_str, n):
            num_list = []
            for i in range(1, n + 1):
                if not str(i) in num_str:
                    num_list.append(str(i))
            return num_list

        def back(num_str):
            nonlocal cur
            nonlocal ans
            if cur >= k:
                return
            if len(num_str) == n:
                cur += 1
                if cur == k:
                    ans = num_str
                    return
                return
            num_list = generate_list(num_str, n)
            for i in num_list:
                back(num_str + i)
        def factorial(n):
            ret = 1
            for i in range(1, n + 1):
                ret *= i
            return ret
        for i in range(1, n + 1):
            fac = factorial(n - 1)
            if factorial(n - 1) < k:
                k = k - fac
            else:
                start = i
                break
        for i in range(start, n + 1):
            back(str(i))
        return ans
