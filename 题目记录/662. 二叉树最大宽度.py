# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        from collections import deque
        ans = 0
        q = deque([(root, 0)])
        while len(q) != 0:
            ans = max(q[-1][1] - q[0][1] + 1, ans)
            for i in range(len(q)):
                tmp = q.popleft()
                if tmp[0].left:
                    q.append((tmp[0].left, tmp[1] * 2))
                if tmp[0].right:
                    q.append((tmp[0].right, tmp[1] * 2 + 1))
        return ans