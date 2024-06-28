# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:        
        paths = 0
        
        def dfs(node, target):
            nonlocal paths
            if node is None:
                return
            if node.val == target:
                paths += 1
            dfs(node.left, target - node.val)
            dfs(node.right, target - node.val)
            
        def preorder(node):
            if node is None:
                return
            dfs(node, targetSum)
            preorder(node.left)
            preorder(node.right)
            
        preorder(root)
        
        return paths