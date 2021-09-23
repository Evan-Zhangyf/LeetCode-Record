class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def reachable(s1, s2):
            if len(s1) == len(s2):
                cnt = False
                for i in range(len(s1)):
                    if s1[i] != s2[i]:
                        if cnt:
                            return False
                        else:
                            cnt = True
                return True
            else:
                return False
        
        wordList.append(beginWord)
        e = [[] for _ in range(len(wordList))]
        end = -1
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                end = i
            for j in range(i + 1, len(wordList)):
                if reachable(wordList[i], wordList[j]):
                    e[i].append(j)
                    e[j].append(i)
        if i == -1:
            return 0
        
        vis = [False] * len(wordList)
        from collections import deque
        q = deque([(len(wordList) - 1, 1)])
        vis[-1] = True
        while len(q) != 0:
            cur = q.popleft()
            for n in e[cur[0]]:
                if n == end:
                    return cur[1] + 1
                if vis[n] == False:
                    q.append((n, cur[1] + 1))
                    vis[n] = True
        return 0

