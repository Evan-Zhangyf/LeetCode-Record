class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        hashmap = {}
        def find(var):
            while hashmap[var] != var:
                var = hashmap[var]
            return var
        for eq in equations:
            if eq[1] == "=":
                if hashmap.get(eq[0]) == None and hashmap.get(eq[3]) == None:
                    hashmap[eq[0]] = eq[0]
                    hashmap[eq[3]] = eq[0]
                if hashmap.get(eq[0]) == None and hashmap.get(eq[3]) != None:
                    hashmap[eq[0]] = eq[3]
                if hashmap.get(eq[0]) != None and hashmap.get(eq[3]) == None:
                    hashmap[eq[3]] = eq[0]
                if hashmap.get(eq[0]) != None and hashmap.get(eq[3]) != None:
                    hashmap[find(eq[0])] = find(eq[3])
        for eq in equations:
            if eq[1] == "!":
                if hashmap.get(eq[0]) == None or hashmap.get(eq[3]) == None:
                    if eq[0] == eq[3]:
                        return False
                    continue
                else:
                    if find(eq[0]) == find(eq[3]):
                        return False
        return True