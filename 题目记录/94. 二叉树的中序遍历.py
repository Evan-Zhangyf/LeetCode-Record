# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#�ݹ鷨
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

#ʹ��ջ����һֱ�����ߵ���ͷ��Ȼ�󿴿���ǰ�ڵ������ҽڵ㣬�еĻ��ͽ����ҽڵ���һ·���ߣ�û�еĻ�������һ���ڵ�鿴�����ҽڵ㣬ֱ���ҵ����ҽڵ��Ϊֹ�������ҽڵ�һ·����ѭ��
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