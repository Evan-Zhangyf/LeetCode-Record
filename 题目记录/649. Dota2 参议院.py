class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        R = deque([])
        D = deque([])
        for i in range(len(senate)):
            if senate[i] == "D":
                D.append(i)
            else:
                R.append(i)
        while len(D) and len(R):
            if D[0] < R[0]:
                tmp = D.popleft()
                D.append(tmp + len(senate))
                R.popleft()
            else:
                tmp = R.popleft()
                R.append(tmp + len(senate))
                D.popleft()
        if len(D):
            return "Dire"
        else:
            return "Radiant"