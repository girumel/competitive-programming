# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        edges = [[] for _ in range(n)]
        safe_nodes = []
        queue = deque()
        
        for i in range(n):
            for j in graph[i]:
                edges[j].append(i)
                indegree[i] += 1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
     
        while queue:
            node = queue.popleft()
            for next_node in edges[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)

        for i in range(n):
            if indegree[i] == 0:
                safe_nodes.append(i)
        
        return safe_nodes