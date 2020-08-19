# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        ans = [[]]
        from collections import deque
        q = deque([[root, 0]])
        while len(q) != 0:
            cur = q.popleft()
            if len(ans) == cur[1] + 1:
                ans[cur[1]].append(cur[0].val)
            else:
                ans.append([cur[0].val])
            if cur[0].left != None:
                q.append([cur[0].left, cur[1] + 1])
            if cur[0].right != None:
                q.append([cur[0].right, cur[1] + 1])
        return ans