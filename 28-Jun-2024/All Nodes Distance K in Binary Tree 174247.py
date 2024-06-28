# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([(target.val, 0)])
        visited = set()
        answer = []

        def dfs(node, parent):
            if node is None:
                return
            if parent:
                graph[node.val].append(parent.val)
            if node.left:
                graph[node.val].append(node.left.val)
                dfs(node.left, node)
            if node.right:
                graph[node.val].append(node.right.val)
                dfs(node.right, node)
        
        dfs(root, None)

        while queue:
            node, distance = queue.popleft()
            if distance == k:
                answer.append(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))
        
        return answer