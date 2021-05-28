# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        from collections import deque
        q = deque([root])
        ans = []
        while len(q):
            ans.append(q[-1].val)
            for i in range(len(q)):
                tmp = q.popleft()
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
        return ans