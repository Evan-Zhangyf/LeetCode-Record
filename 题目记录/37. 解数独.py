class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def back(index):
            nonlocal find
            if index == len(empty_list):
                find = True
                return
            x = empty_list[index][0]
            y = empty_list[index][1]
            for i in range(1, 10):
                if row[x][i] == False and col[y][i] == False and block[x//3][y//3][i] == False:
                    row[x][i] = True
                    col[y][i] = True
                    block[x//3][y//3][i] = True
                    board[x][y] = str(i)
                    back(index + 1)
                    if find:
                        return
                    row[x][i] = False
                    col[y][i] = False
                    block[x//3][y//3][i] = False
                    board[x][y] = "."


        row = [[False] * 10 for _ in range(9)]
        col = [[False] * 10 for _ in range(9)]
        block = [[[False] * 10 for _ in range(3)] for _ in range(3)]
        find = False
        empty_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_list.append((i, j))
                else:
                    num = int(board[i][j])
                    row[i][num] = True
                    col[j][num] = True
                    block[i//3][j//3][num] = True
        back(0)
        return