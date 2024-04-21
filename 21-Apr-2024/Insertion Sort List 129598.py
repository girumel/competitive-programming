# Problem: Insertion Sort List - https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = head
        previous = dummy
        next_node = None

        while current:
            next_node = current.next

            while previous.next and previous.next.val < current.val:
                previous = previous.next

            current.next = previous.next
            previous.next = current
            previous = dummy
            current = next_node

        return dummy.next