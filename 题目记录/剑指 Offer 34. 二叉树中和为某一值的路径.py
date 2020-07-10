# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        #特判
        if root == None:
            return []
        #是叶子节点
        if root.left == None and root.right == None:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        #非叶子节点
        path = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        for i in range(len(path)):
            path[i] = [root.val] + path[i]
        return path

