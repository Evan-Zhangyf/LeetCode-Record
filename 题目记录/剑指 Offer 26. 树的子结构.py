# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rootcontain(self, A, B):
        if B != None:
            if A == None:
                return False
            elif A.val != B.val:
                return False
            else:
                return self.rootcontain(A.left, B.left) and self.rootcontain(A.right, B.right)
        else:
            return True

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B == None:
            return False
        if A == None:
            return False
        return self.rootcontain(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)