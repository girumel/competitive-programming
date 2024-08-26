# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []

        def helper(root):
                if not root:
                    return
                for child in root.children:
                    helper(child)
                order.append(root.val)
    
        helper(root)
        
        return order