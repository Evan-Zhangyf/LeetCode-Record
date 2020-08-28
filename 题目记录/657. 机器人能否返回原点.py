class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        for i in moves:
            if i == "U":
                pos[1] += 1
            if i == "D":
                pos[1] -= 1
            if i == "L":
                pos[0] -= 1
            if i == "R":
                pos[0] += 1
        return pos == [0, 0]