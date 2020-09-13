class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[0] * len(board[0]) for _ in range(len(board))]

        def dfs(pos, cur_word):
            nonlocal visited
            if cur_word + 1 == len(word):
                return True
            # up
            if pos[0] - 1 >= 0 and visited[pos[0]-1][pos[1]] == 0 and board[pos[0]-1][pos[1]] == word[cur_word+1]:
                visited[pos[0]][pos[1]] = 1
                if dfs((pos[0] - 1, pos[1]), cur_word + 1):
                    return True
                visited[pos[0]][pos[1]] = 0
            # down
            if pos[0] + 1 < len(board) and visited[pos[0]+1][pos[1]] == 0 and board[pos[0]+1][pos[1]] == word[cur_word+1]:
                visited[pos[0]][pos[1]] = 1
                if dfs((pos[0] + 1, pos[1]), cur_word + 1):
                    return True
                visited[pos[0]][pos[1]] = 0
            # left
            if pos[1] - 1 >= 0 and visited[pos[0]][pos[1] - 1] == 0 and board[pos[0]][pos[1]-1] == word[cur_word+1]:
                visited[pos[0]][pos[1]] = 1
                if dfs((pos[0], pos[1] - 1), cur_word + 1):
                    return True
                visited[pos[0]][pos[1]] = 0
            # right
            if pos[1] + 1 < len(board[0]) and visited[pos[0]][pos[1]+1] == 0 and board[pos[0]][pos[1]+1] == word[cur_word+1]:
                visited[pos[0]][pos[1]] = 1
                if dfs((pos[0], pos[1] + 1), cur_word + 1):
                    return True
                visited[pos[0]][pos[1]] = 0
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # dfs + 剪枝
                    if dfs((i, j), 0):
                        return True
        return False