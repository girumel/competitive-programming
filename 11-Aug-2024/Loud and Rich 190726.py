# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        answer = [-1] * n
        graph = [[] for _ in range(n)]
        
        for u, v in richer:
            graph[v].append(u)
        
        def dfs(node):
            if answer[node] >= 0:
                return answer[node]
            answer[node] = node
            for child in graph[node]:
                if quiet[dfs(child)] < quiet[answer[node]]:
                    answer[node] = answer[child]
            return answer[node]
        
        for i in range(n):
            dfs(i)
        
        return answer