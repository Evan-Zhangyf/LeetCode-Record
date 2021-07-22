"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        def copy_node(n):
            if n == None:
                return None
            return Node(n.val)
        node_list = []
        cur = head
        idx = {}
        i = 0
        while cur:
            node_list.append(cur)
            idx[cur] = i
            cur = cur.next
            i += 1
        idx_map = []
        for n in node_list:
            if n.random == None:
                idx_map.append(-1)
            else:
                idx_map.append(idx[n.random])
        new_head = copy_node(head)
        cur1 = head
        cur = new_head
        copy_list = [new_head]
        while cur1.next:
            cur.next = copy_node(cur1.next)
            cur = cur.next
            cur1 = cur1.next
            copy_list.append(cur)
        for i in range(len(copy_list)):
            if idx_map[i] == -1:
                copy_list[i].random = None
            else:
                copy_list[i].random = copy_list[idx_map[i]]
        return new_head