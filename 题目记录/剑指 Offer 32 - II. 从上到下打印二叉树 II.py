# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        ans = []
        q = deque()
        q.append(root)
        while len(q) != 0:
            tmp = []
            for i in range(len(q)):
                cur = q.popleft()
                tmp.append(cur.val)
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
            ans.append(tmp)
        return ans