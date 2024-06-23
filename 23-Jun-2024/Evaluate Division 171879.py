# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (u, v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1 / value

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            # if start == end:
            #     return 1.0
            if end in graph[start]:
                return graph[start][end]
            visited.add(start)
            for neighbor in graph[start]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return graph[start][neighbor] * result
            # visited.remove(start)
            return -1.0

        return [dfs(start, end, set()) for start, end in queries]