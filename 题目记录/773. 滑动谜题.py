class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque
        from copy import deepcopy
        q = deque([board])
        s = deque([0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    p = deque([(i, j)])
        vis = {}
        vis[str(board)] = True
        while len(q):
            cur = q.popleft()
            pos = p.popleft()
            step = s.popleft()
            if cur == [[1,2,3],[4,5,0]]:
                return step
            # up
            if pos[0] - 1 >= 0:
                cur[pos[0] - 1][pos[1]], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0] - 1][pos[1]]
                if not vis.get(str(cur)):
                    vis[str(cur)] = True
                    q.append(deepcopy(cur))
                    p.append((pos[0] - 1, pos[1]))
                    s.append(step + 1)
                cur[pos[0] - 1][pos[1]], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0] - 1][pos[1]]
            # down
            if pos[0] + 1 < len(board):
                cur[pos[0] + 1][pos[1]], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0] + 1][pos[1]]
                if not vis.get(str(cur)):
                    vis[str(cur)] = True
                    q.append(deepcopy(cur))
                    p.append((pos[0] + 1, pos[1]))
                    s.append(step + 1)
                cur[pos[0] + 1][pos[1]], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0] + 1][pos[1]]
            # left
            if pos[1] - 1 >= 0:
                cur[pos[0]][pos[1] - 1], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0]][pos[1] - 1]
                if not vis.get(str(cur)):
                    vis[str(cur)] = True
                    q.append(deepcopy(cur))
                    p.append((pos[0], pos[1] - 1))
                    s.append(step + 1)
                cur[pos[0]][pos[1] - 1], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0]][pos[1] - 1]
            # right
            if pos[1] + 1 < len(board[0]):
                cur[pos[0]][pos[1] + 1], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0]][pos[1] + 1]
                if not vis.get(str(cur)):
                    vis[str(cur)] = True
                    q.append(deepcopy(cur))
                    p.append((pos[0], pos[1] + 1))
                    s.append(step + 1)
                cur[pos[0]][pos[1] + 1], cur[pos[0]][pos[1]] = cur[pos[0]][pos[1]], cur[pos[0]][pos[1] + 1]
        return -1


