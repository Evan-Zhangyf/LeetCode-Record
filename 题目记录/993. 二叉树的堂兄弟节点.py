# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        from collections import deque
        q = deque([root])
        while q:
            cnt = 0
            for i in range(len(q)):
                tmp = q.popleft()
                if tmp.val == x or tmp.val == y:
                    cnt += 1
                if tmp.left and tmp.right:
                    if (tmp.left.val, tmp.right.val) == (x, y) or  (tmp.left.val, tmp.right.val) == (y, x):
                        return False
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            if cnt == 1:
                return False
            if cnt == 2:
                return True
        return False
