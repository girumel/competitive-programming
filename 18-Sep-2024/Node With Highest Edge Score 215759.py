# Problem: Node With Highest Edge Score - https://leetcode.com/problems/node-with-highest-edge-score/description/

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        nodes = [0]*n
        
        for i in range(n):
            nodes[edges[i]] += i
        return nodes.index(max(nodes))