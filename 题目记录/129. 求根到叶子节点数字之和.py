# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nums = []
        def back(num, cur):
            num = num * 10 + cur.val
            if cur.left == None and cur.right == None:
                nums.append(num)
                return
            if cur.left:
                back(num, cur.left)
            if cur.right:
                back(num, cur.right)
        if root == None:
            return 0
        else:
            back(0, root)
        ans = 0
        for i in nums:
            ans += i
        return ans