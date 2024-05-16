# Problem: Binary Tree Postorder Traversal - https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        stack = []
        result = []

        current = root
        while stack or current:
            while current:
                stack.append(current)
                result.insert(0, current.val)
                current = current.right
            
            current = stack.pop()
            current = current.left
        
        return result