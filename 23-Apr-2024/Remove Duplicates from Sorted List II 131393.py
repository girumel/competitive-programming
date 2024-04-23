# Problem: Remove Duplicates from Sorted List II - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        previous = dummy
        current = head

        while current and current.next:
            if current.val == current.next.val:
                while current.next and current.val == current.next.val:
                        current = current.next
                current = current.next
                previous.next = current
            else:
                previous = previous.next
                current = current.next

        return dummy.next