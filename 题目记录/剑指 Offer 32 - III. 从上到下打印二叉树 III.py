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
        from collections import deque
        q = deque([root])
        ans = []
        layer = 0
        while len(q) != 0:
            ans.append([])
            if layer % 2 == 0:
                for i in range(len(q)):
                    cur = q.popleft()
                    ans[layer].append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            else:
                 for i in range(len(q)):
                    cur = q.pop()
                    ans[layer].append(cur.val)
                    if cur.right:
                        q.appendleft(cur.right)
                    if cur.left:
                        q.appendleft(cur.left)
            layer += 1
        return ans         