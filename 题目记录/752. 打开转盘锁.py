class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        dead_dic = {}
        for num in deadends:
            dead_dic[num] = True
        if dead_dic.get(target) or dead_dic.get("0000"):
            return -1
        from collections import deque
        q = deque([("0000", 0)])
        vis = {}
        vis["0000"] = True
        while len(q) != 0:
            tmp = q.popleft()
            s = tmp[1]
            cur = tmp[0]
            if cur == target:
                return s
            arr = []
            for i in range(4):
                arr.append(cur[i])
            for i in range(4):
                arr[i] = str((int(arr[i]) + 1) % 10)
                tmp_str = "".join(arr)
                if not dead_dic.get(tmp_str) and not vis.get(tmp_str):
                    vis[tmp_str] = True
                    q.append((tmp_str, s + 1))
                arr[i] = str((int(arr[i]) - 2) % 10)
                tmp_str = "".join(arr)
                if not dead_dic.get(tmp_str) and not vis.get(tmp_str):
                    vis[tmp_str] = True
                    q.append((tmp_str, s + 1))
                arr[i] = str((int(arr[i]) + 1) % 10)
        return -1