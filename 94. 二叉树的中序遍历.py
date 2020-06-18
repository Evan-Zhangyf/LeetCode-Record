# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#递归法
class Solution:
    def __init__(self):
        self.node_list = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return self.node_list
        self.inorderTraversal(root.left)
        self.node_list.append(root.val)
        self.inorderTraversal(root.right)
        return self.node_list

#使用栈，先一直向左走到尽头，然后看看当前节点有无右节点，有的话就进入右节点再一路左走，没有的话回溯上一个节点查看有无右节点，直到找到有右节点的为止，进入右节点一路左走循环
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        node_list = []
        node_stack = []
        cur = root
        while cur != None or len(node_stack)>0:
            while cur != None:
                node_stack.append(cur)
                cur = cur.left
            cur = node_stack.pop()
            node_list.append(cur.val)
            cur = cur.right
        return node_list