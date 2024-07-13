# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode()
        current = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next