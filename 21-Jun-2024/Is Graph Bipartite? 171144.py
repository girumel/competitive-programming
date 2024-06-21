# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n

        def dfs(node, color):
            if colors[node] != 0:
                return colors[node] == color
            colors[node] = color
            
            for neighbor in graph[node]:
                if not dfs(neighbor, -color):
                    return False
            return True
        
        # dfs(0, 1)

        for node in range(n):
            if colors[node] == 0 and not dfs(node, 1):
                return False

        return True