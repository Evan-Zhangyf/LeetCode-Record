# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root.left == None:
            return -1
        tmp = [root.val, root.left.val, root.right.val]
        tmp1 = self.findSecondMinimumValue(root.left)
        tmp2 = self.findSecondMinimumValue(root.right)
        if tmp1 != -1:
            tmp.append(tmp1)
        if tmp2 != -1:
            tmp.append(tmp2)
        tmp.sort()
        for i in range(1, len(tmp)):
            if tmp[i] != tmp[0]:
                return tmp[i]
        return -1
            