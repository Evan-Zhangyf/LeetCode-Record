class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(land)):
            flag = False
            for j in range(len(land[0])):
                if land[i][j] == 0:
                    flag = False
                elif land[i][j] == 2:
                    flag = True
                elif land[i][j] == 1:
                    if flag != True:
                        # length
                        l = j
                        while l < len(land[0]) and land[i][l] == 1:
                            land[i][l] = 2
                            l += 1
                        l -= 1
                        land[i][j] = 1

                        # width
                        w = i
                        while w < len(land) and land[w][j] == 1:
                            land[w][j] = 2
                            w += 1
                        w -= 1
                        
                        ans.append([i, j, w, l])
        return ans