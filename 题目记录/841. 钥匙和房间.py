class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        visited[0] = 1
        s = [0]
        n = 0
        while len(s) != 0:
            cur = s.pop()
            n += 1
            for room in rooms[cur]:
                if visited[room] == 0:
                    visited[room] = 1
                    s.append(room)
        return n == len(rooms)