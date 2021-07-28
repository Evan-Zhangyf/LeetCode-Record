# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        prev = {}
        def mark(root, target):
            nonlocal prev
            if root == target:
                return
            if root.left:
                prev[root.left] = root
                mark(root.left, target)
            if root.right:
                prev[root.right] = root
                mark(root.right, target)

        mark(root, target)
        # bfs
        from collections import deque
        q = deque([target])
        vis = {}
        vis[target] = True
        layer = 0
        while len(q) != 0:
            layer += 1
            for i in range(len(q)):
                cur = q.popleft()
                if prev.get(cur) != None and vis.get(prev[cur]) == None:
                    q.append(prev[cur])
                    vis[prev[cur]] = True
                if cur.left and vis.get(cur.left) == None:
                    q.append(cur.left)
                    vis[cur.left] = True
                if cur.right and vis.get(cur.right) == None:
                    q.append(cur.right)
                    vis[cur.right] = True
            if layer == k:
                ans = []
                for i in range(len(q)):
                    ans.append(q[i].val)
                return ans
        return []
