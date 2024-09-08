# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return False
            parent[root_x] = root_y
            return True
        
        for edge in edges:
            if not union(edge[0], edge[1]):
                return edge
        
        return []