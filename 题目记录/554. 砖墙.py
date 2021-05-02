class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = {}
        max_bricks = 0
        for row in wall:
            cur_len = row[0]
            for i in range(1, len(row)):
                if dic.get(cur_len) != None:
                    dic[cur_len] += 1
                    max_bricks = max(max_bricks, dic[cur_len])
                else:
                    dic[cur_len] = 1
                    max_bricks = max(max_bricks, dic[cur_len])
                cur_len += row[i]
        return len(wall) - max_bricks