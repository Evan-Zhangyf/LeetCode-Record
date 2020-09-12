# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return []
        from collections import deque
        q = deque([(root, 0)])
        ans = []
        # bfs
        while len(q) != 0:
            cur = q.popleft()
            if cur[1] >= len(ans):
                ans.append([cur[0].val, 1])
            else:
                ans[cur[1]][0] += cur[0].val
                ans[cur[1]][1] += 1
            if cur[0].left != None:
                q.append((cur[0].left, cur[1] + 1))
            if cur[0].right != None:
                q.append((cur[0].right, cur[1] + 1))
    
        for i in range(len(ans)):
            ans[i] = ans[i][0] / ans[i][1]
        return ans