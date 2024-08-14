# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        longest = -1

        for node in range(n):
            if visited[node]:
                continue

            current = node
            cycle = []

            while current != -1 and not visited[current]:
                visited[current] = True
                cycle.append(current)
                current = edges[current]

            if current == -1:
                continue

            length = len(cycle)
            start = float('inf')
            for k, v in enumerate(cycle):
                if v == current:
                    start = k
                    break
            longest = max(longest, length - start)

        return longest