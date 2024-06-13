# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reachable = set()
        min_vertices = []

        for nodeA, nodeB in edges:
            reachable.add(nodeB)
        
        for vertex in range(n):
            if vertex not in reachable:
                min_vertices.append(vertex)
        
        return min_vertices