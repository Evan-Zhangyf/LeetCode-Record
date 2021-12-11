class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = []
        self.vote = []
        tmp = []
        for i in range(len(persons)):
            tmp.append((times[i], persons[i]))
        tmp.sort(key = lambda x : x[0])
        vote_dict = defaultdict(int)
        candidate = -1
        for i in range(len(tmp)):
            if i != 0 and tmp[i][0] != tmp[i-1][0]:
                self.times.append(tmp[i-1][0])
                self.vote.append(candidate)
            vote_dict[tmp[i][1]] += 1
            if vote_dict[tmp[i][1]] >= vote_dict[candidate]:
                candidate = tmp[i][1]
        self.times.append(tmp[-1][0])
        self.vote.append(candidate)


    def q(self, t: int) -> int:
        l = 0
        r = len(self.times) - 1
        while l < r:
            m = (l + r + 1) // 2
            if self.times[m] > t:
                r = m - 1
            else:
                l = m
        return self.vote[l]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)