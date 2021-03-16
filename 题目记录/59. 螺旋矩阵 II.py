class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        vx = 1
        vy = 0
        x = 0
        y = 0
        cur = 1
        while True:
            matrix[y][x] = cur
            cur += 1
            if x + vx >= len(matrix[0]):
                vx = 0
                vy = 1
            elif x + vx < 0:
                vx = 0
                vy = -1
            elif y + vy >= len(matrix):
                vx = -1
                vy = 0
            elif y + vy < 0:
                vx = 1
                vy = 0
            elif matrix[y + vy][x + vx] != 0:
                if vy == 0:
                    vy = vx
                    vx = 0
                else:
                    vx = -vy
                    vy = 0
            if x + vx >= len(matrix[0]) or x + vx < 0 or y + vy >= len(matrix) or y + vy < 0 or matrix[y + vy][x + vx] != 0:
                break
            x = x + vx
            y = y + vy
        return matrix