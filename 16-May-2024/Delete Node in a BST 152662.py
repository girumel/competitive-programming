# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderSuccessor(self, root):
        temp_right = root.right
        while temp_right.left:
            temp_right = temp_right.left
        
        return temp_right

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        if key == root.val:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

        root.val = self.inorderSuccessor(root).val

        root.right = self.deleteNode(root.right, root.val)

        return root



