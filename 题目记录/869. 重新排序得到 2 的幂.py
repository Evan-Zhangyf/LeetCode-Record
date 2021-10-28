class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = []
        while n:
            digits.append(n % 10)
            n = n // 10
        
        cur = []
        vis = [False] * len(digits)

        def check(d):
            s = 0
            for i in range(len(d)):
                s *= 10
                s += d[i]
            return (s & (s - 1)) == 0
            

        def back(pos):
            if pos == len(digits):
                return check(cur)
            for i in range(len(digits)):
                if vis[i] == False:
                    if pos == 0 and digits[i] == 0:
                        continue
                    vis[i] = True
                    cur.append(digits[i])
                    if back(pos + 1):
                        return True
                    cur.pop()
                    vis[i] = False
            return False
        return back(0)