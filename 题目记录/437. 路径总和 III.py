# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root == None:
            return 0
        ans = 0 
        def helper(root, targetSum):
            if root == None:
                return 0
            ret = helper(root.left, targetSum - root.val) +  helper(root.right, targetSum - root.val)
            if root.val == targetSum:
                ret += 1
            return ret
        s = [root]
        while s:
            tmp = s.pop()
            ans += helper(tmp, targetSum)
            if tmp.left:
                s.append(tmp.left)
            if tmp.right:
                s.append(tmp.right)
        return ans