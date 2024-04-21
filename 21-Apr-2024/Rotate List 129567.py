# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        current, length = head, 0
        while current:
            current = current.next
            length += 1

        k %= length
        if k == 0:
            return head

        slow = fast = head
        for _ in range(k):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        new = slow.next
        slow.next = None
        fast.next = head

        return new