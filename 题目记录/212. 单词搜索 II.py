class node:
    def __init__(self):
        self.next = {}
        self.is_word = False
        self.word = ""

class trie:
    def __init__(self):
        self.root = node()
    def insert(self, word):
        cur = self.root
        for l in word:
            if not l in cur.next:
                cur.next[l] = node()
            cur = cur.next[l]
        cur.is_word = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = trie()
        for w in words:
            t.insert(w)
        vis = [[False] * len(board[0]) for _ in range(len(board))]
        ans = []
        def back(i, j, node):
            if node.is_word == True:
                ans.append(node.word)
                node.is_word = False
            # up
            if i > 0 and board[i-1][j] in node.next and vis[i-1][j] == False:
                vis[i-1][j] = True
                back(i-1, j, node.next[board[i-1][j]])
                vis[i-1][j] = False
            # down
            if i < len(board) - 1 and board[i+1][j] in node.next and vis[i+1][j] == False:
                vis[i+1][j] = True
                back(i+1, j, node.next[board[i+1][j]])
                vis[i+1][j] = False
            # left
            if j > 0 and board[i][j-1] in node.next and vis[i][j-1] == False:
                vis[i][j-1] = True
                back(i, j-1, node.next[board[i][j-1]])
                vis[i][j-1] = False
            # right
            if j < len(board[0]) - 1 and board[i][j+1] in node.next and vis[i][j+1] == False:
                vis[i][j+1] = True
                back(i, j+1, node.next[board[i][j+1]])
                vis[i][j+1] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in t.root.next:
                    vis[i][j] = True
                    back(i, j, t.root.next[board[i][j]])
                    vis[i][j] = False
        return ans