# Problem: Maximum Width of Binary Tree - https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 0)])
        max_width = 0

        while queue:
            nodes_count = len(queue)
            if nodes_count == 1:
                leftmost = 0
            rightmost = queue[-1][1]
            leftmost = queue[0][1]
            max_width = max(max_width, rightmost - leftmost + 1)
            for _ in range(nodes_count):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width