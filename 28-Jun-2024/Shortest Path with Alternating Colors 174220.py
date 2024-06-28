# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[[], []] for _ in range(n)]
        for a, b in redEdges:
            graph[a][0].append(b)
        for u, v in blueEdges:
            graph[u][1].append(v)
        
        answer = [0] + [-1] * (n-1)
        visited = set()
        queue = deque([(0, 0, 0), (0, 1, 0)])
        
        while queue:
            node, color, dist = queue.popleft()
            for neighbor in graph[node][color]:
                if (neighbor, 1 - color) not in visited:
                    visited.add((neighbor, 1 - color))
                    if answer[neighbor] == -1 or answer[neighbor] > dist + 1:
                        answer[neighbor] = dist + 1
                    queue.append((neighbor, 1 - color, dist + 1))

        return answer