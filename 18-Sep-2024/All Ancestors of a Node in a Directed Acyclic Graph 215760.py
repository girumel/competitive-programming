# Problem: All Ancestors of a Node in a Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = []

        graph = defaultdict(list)
        for u, v in edges:
            graph[v].append(u)

        for i in range(n):
            q = deque([i])
            visited = set()
            while q:
                node = q.popleft()
                for parent in graph[node]:
                    if parent not in visited:
                        q.append(parent)
                        visited.add(parent)
            answer.append(sorted(list(visited)))

        return answer