# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        max_detonations = 0

        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j:
                    distance = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                    if distance <= r1:
                        adj_list[i].append(j)
                    if distance <= r2:
                        adj_list[j].append(i)

        def dfs(i, visited):
            if i in visited:
                return 0
            visited.add(i)
            for neighbor in adj_list[i]:
                dfs(neighbor, visited)
            return len(visited)

        for i in range(len(bombs)):
            max_detonations = max(max_detonations, dfs(i, set()))

        return max_detonations