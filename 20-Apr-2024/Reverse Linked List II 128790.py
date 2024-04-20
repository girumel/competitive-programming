# Problem: Reverse Linked List II - https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        
        current, previous = head, None

        while left > 1:
            previous = current
            current = current.next
            left, right = left - 1, right - 1

        right_tail, left_tail = current, previous

        while right:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            right -= 1

        if left_tail:
            left_tail.next = previous
        else:
            head = previous

        right_tail.next = current
        return head