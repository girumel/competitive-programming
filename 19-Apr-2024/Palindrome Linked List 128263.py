# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev_node = None
        while slow:
            next_node = slow.next
            slow.next = prev_node
            prev_node = slow
            slow = next_node

        while prev_node:
            if head.val != prev_node.val:
                return False
            head = head.next
            prev_node = prev_node.next
        
        return True
        