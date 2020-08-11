class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        mark = [[0] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and mark[i][j] == 0 and (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1):
                    # dfs
                    s = [(i, j)]
                    mark[i][j] = 1
                    while s != []:
                        cur = s.pop()
                        # up
                        if cur[0] - 1 >= 0 and board[cur[0]-1][cur[1]] == 'O' and mark[cur[0]-1][cur[1]] == 0:
                            mark[cur[0]-1][cur[1]] = 1
                            s.append((cur[0]-1, cur[1]))
                        # down
                        if cur[0] + 1 < len(board) and board[cur[0]+1][cur[1]] == 'O' and mark[cur[0]+1][cur[1]] == 0:
                            mark[cur[0]+1][cur[1]] = 1
                            s.append((cur[0]+1, cur[1]))
                        # left
                        if cur[1] - 1 >= 0 and board[cur[0]][cur[1]-1] == 'O' and mark[cur[0]][cur[1]-1] == 0:
                            mark[cur[0]][cur[1]-1] = 1
                            s.append((cur[0], cur[1]-1))
                        # right
                        if cur[1] + 1 < len(board[0]) and board[cur[0]][cur[1]+1] == 'O' and mark[cur[0]][cur[1]+1] == 0:
                            mark[cur[0]][cur[1]+1] = 1
                            s.append((cur[0], cur[1]+1))
        # 填充未标记的o
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and mark[i][j] == 0:
                    board[i][j] = 'X'