# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        queries = sorted(enumerate(queries), key=lambda x: x[1][2])
        parent = [i for i in range(n)]
        answer = [False] * len(queries)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        def connected(x, y):
            return find(x) == find(y)

        i = 0
        for j, (p, q, limit) in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            answer[j] = connected(p, q)
        return answer