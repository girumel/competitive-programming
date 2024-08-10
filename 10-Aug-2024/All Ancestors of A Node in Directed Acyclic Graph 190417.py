# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        ancestors = {}
        
        for edge in edges:
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            if node in ancestors:
                return ancestors[node]
            ancestors[node] = set()
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node] |= dfs(parent)
            return ancestors[node]
        
        for i in range(n):
            dfs(i)
        return [sorted(list(ancestors[i])) for i in range(n)]