class WordDictionary:

    def __init__(self):
        self.node = {}
        self.is_leaf = False

    def addWord(self, word: str) -> None:
        cur = self
        for i in range(len(word)):
            if cur.node.get(word[i]):
                cur = cur.node[word[i]]
            else:
                cur.node[word[i]] = WordDictionary()
                cur = cur.node[word[i]]
        cur.is_leaf = True

    def search(self, word: str) -> bool:
        def find(root, pos):
            if pos == len(word):
                return root.is_leaf
            if word[pos] == ".":
                for k in root.node:
                    if find(root.node[k], pos + 1):
                        return True 
                return False
            else:
                if root.node.get(word[pos]):
                    return find(root.node[word[pos]], pos + 1)
                else:
                    return False
            
        return find(self, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)