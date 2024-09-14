# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [(0, 0, root)] # (row, col, val)
        order = defaultdict(list)
        while queue:
            new_queue = []
            for row, col, node in queue:
                order[col].append((row, node.val))
                if node.left:
                    new_queue.append((row + 1, col - 1, node.left))
                if node.right:
                    new_queue.append((row + 1, col + 1, node.right))
            queue = new_queue

        traversal = []
        for col in sorted(order.keys()):
            traversal.append([val for row, val in sorted(order[col])])

        return traversal