# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        items = set()
        
        dummy_node = head
        while dummy_node:
            if dummy_node in items:
                return dummy_node
            items.add(dummy_node)
            dummy_node = dummy_node.next
        
        return None
    