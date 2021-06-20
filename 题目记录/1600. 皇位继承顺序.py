class ThroneInheritance:

    def __init__(self, kingName: str):
        from collections import deque
        self.e = defaultdict(deque)
        self.king = kingName
        self.dead = {}

    def birth(self, parentName: str, childName: str) -> None:
        self.e[parentName].appendleft(childName)

    def death(self, name: str) -> None:
        self.dead[name] = True

    def getInheritanceOrder(self) -> List[str]:
        curOrder = []
        s = [self.king]
        while s != []:
            cur = s.pop()
            curOrder.append(cur)
            for person in self.e[cur]:
                s.append(person)
        ans = []
        for person in curOrder:
            if not self.dead.get(person):
                ans.append(person)
        return ans



# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()