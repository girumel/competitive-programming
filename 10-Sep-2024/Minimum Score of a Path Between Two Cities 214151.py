# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        min_score = float('inf')

        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(city_a, city_b):
            root_a, root_b = find(city_a), find(city_b)
            if root_a != root_b:
                if rank[root_a] > rank[root_b]:
                    parent[root_b] = root_a
                elif rank[root_a] < rank[root_b]:
                    parent[root_a] = root_b
                else:
                    parent[root_b] = root_a
                    rank[root_a] += 1

        for city_a, city_b, _ in roads:
            union(city_a, city_b)

        for city_a, city_b, score in roads:
            if find(city_a) == find(1):
                min_score = min(min_score, score)

        return min_score