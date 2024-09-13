# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i, (x, y) in enumerate(stones):
            for j, (x1, y1) in enumerate(stones):
                if x == x1 or y == y1:
                    graph[i].append(j)
                    
        visited = set()
        def dfs(i):
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)
                    
        count = 0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                count += 1
                
        return len(stones) - count