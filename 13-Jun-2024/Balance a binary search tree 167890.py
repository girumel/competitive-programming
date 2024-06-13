# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_vals = []

        def inorder_traversal(node):
            if node is None:
                return
            inorder_traversal(node.left)
            node_vals.append(node.val)
            inorder_traversal(node.right)
        
        inorder_traversal(root)
        # print(*node_vals)

        def balance_bst(left, right):
            if left > right:
                return None
          
            mid = (left + right) // 2
            node = TreeNode(node_vals[mid])
          
            node.left = balance_bst(left, mid - 1)
            node.right = balance_bst(mid + 1, right)
            return node

        return balance_bst(0, len(node_vals) - 1)