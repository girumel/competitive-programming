# Problem: Detect Cycle in an Undirected Graph - https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		visited = [False] * V
		
		def dfs(graph, v, visited, parent):
            visited[v] = True
        
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    if dfs(graph, neighbor, visited, v):
                        return True
                elif neighbor != parent:
                    return True
        
            return False

        for v in range(V):
            if not visited[v]:
                if dfs(adj, v, visited, -1):
                    return 1
    
        return 0