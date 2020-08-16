class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        orgin_color = image[sr][sc]
        visited = [[0] * len(image[0]) for _ in range(len(image))]
        s = [[sr, sc]]
        visited[sr][sc] = 1
        image[sr][sc] = newColor
        while s != []:
            cur = s.pop()
            # up
            if cur[0] - 1 >= 0 and image[cur[0]-1][cur[1]] == orgin_color and visited[cur[0]-1][cur[1]] == 0:
                image[cur[0]-1][cur[1]] = newColor
                visited[cur[0]-1][cur[1]] = 1
                s.append([cur[0] - 1, cur[1]])
            # down
            if cur[0] + 1 < len(image) and image[cur[0]+1][cur[1]] == orgin_color and visited[cur[0]+1][cur[1]] == 0:
                image[cur[0]+1][cur[1]] = newColor
                visited[cur[0]+1][cur[1]] = 1
                s.append([cur[0] + 1, cur[1]])
            # left
            if cur[1] - 1 >= 0 and image[cur[0]][cur[1]-1] == orgin_color and visited[cur[0]][cur[1]-1] == 0:
                image[cur[0]][cur[1]-1] = newColor
                visited[cur[0]][cur[1]-1] = 1
                s.append([cur[0], cur[1] - 1])
            # right
            if cur[1] + 1 < len(image[0]) and image[cur[0]][cur[1]+1] == orgin_color and visited[cur[0]][cur[1]+1] == 0:
                image[cur[0]][cur[1]+1] = newColor
                visited[cur[0]][cur[1]+1] = 1
                s.append([cur[0], cur[1] + 1])
        return image
        