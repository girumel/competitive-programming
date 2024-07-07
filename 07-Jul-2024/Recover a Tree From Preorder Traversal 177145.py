# Problem: Recover a Tree From Preorder Traversal - https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        n = len(traversal)
        i = 0
        
        def dfs(level):
            nonlocal i
            if i >= n:
                return None
            j = i
            while j < n and traversal[j] == '-':
                j += 1
            if j - i != level:
                return None
            i = j
            val = 0
            while i < n and traversal[i] != '-':
                val = val * 10 + int(traversal[i])
                i += 1
            root = TreeNode(val)
            root.left = dfs(level + 1)
            root.right = dfs(level + 1)
            
            return root
        
        return dfs(0)