# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def helper(l, h):
            if l > h:
                return []
            ans = []
            if l == h:
                return [TreeNode(l)]
            for i in range(l, h + 1):
                l_tree = helper(l, i - 1)
                r_tree = helper(i + 1, h)
                if len(l_tree) == 0:
                    for b in r_tree:
                        ans.append(TreeNode(i, None, b))
                elif len(r_tree) == 0:
                    for a in l_tree:
                        ans.append(TreeNode(i, a, None))
                else:
                    for a in l_tree:
                        for b in r_tree:
                            ans.append(TreeNode(i, a, b))
            return ans
        return helper(1, n)