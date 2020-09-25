# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        num_list = []
        def dfs(root):
            if not root:
                return
            nonlocal num_list
            dfs(root.left)
            num_list.append(root.val)
            dfs(root.right)
        dfs(root)
        ans = []
        max_len = -1
        cur_len = 1
        if len(num_list) <= 1:
            return num_list
        print(num_list)
        for i in range(1, len(num_list)):
            if num_list[i] == num_list[i-1]:
                cur_len += 1
            else:
                if cur_len == max_len:
                    ans.append(num_list[i-1])
                elif cur_len > max_len:
                    ans = [num_list[i-1]]
                    max_len = cur_len
                cur_len = 1
        if cur_len == max_len:
            ans.append(num_list[-1])
        elif cur_len > max_len:
            ans = [num_list[-1]]
        return ans