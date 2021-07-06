class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        idx = {}
        head = []
        for i in range(len(orders)):
            if not idx.get(orders[i][2]):
                idx[orders[i][2]] = 1
                head.append(orders[i][2])
        head.sort()
        for i in range(len(head)):
            idx[head[i]] = i + 1
        head = ["Table"] + head
        ans = []
        table = {}
        for bill in orders:
            if table.get(bill[1]):
                table[bill[1]][idx[bill[2]]] = str(int(table[bill[1]][idx[bill[2]]]) + 1)
            else:
                table[bill[1]] = ["0"] * len(head)
                table[bill[1]][0] = bill[1]
                table[bill[1]][idx[bill[2]]] = "1"
        ans = []
        for bill in table.values():
            ans.append(bill)
        ans.sort(key = lambda x : int(x[0]))
        return [head] + ans