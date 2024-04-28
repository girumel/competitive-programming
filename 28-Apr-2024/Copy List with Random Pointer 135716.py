# Problem: Copy List with Random Pointer - https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        node = head
        
        while node:
            new_node = Node(node.val, node.next, None)
            node.next = new_node
            node = new_node.next
        node = head
        
        while node:
            if node.random:
                node.next.random = node.random.next
            else:
                node.next.random = None
            node = node.next.next
        old_list = head
        new_list = head.next
        new_head = head.next
        
        while old_list:
            old_list.next = old_list.next.next
            if new_list.next:
                new_list.next = new_list.next.next
            else:
                new_list.next = None
            old_list = old_list.next
            new_list = new_list.next
        
        return new_head