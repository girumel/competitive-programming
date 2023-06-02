# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        items = set()
        
        dummy_node = head
        while dummy_node:
            if dummy_node in items:
                return True
            items.add(dummy_node)
            dummy_node = dummy_node.next
        
        return False