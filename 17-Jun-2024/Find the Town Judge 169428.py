# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = {}
        
        for a, b in trust:
            trusted[a] = trusted.get(a, 0) - 1
            trusted[b] = trusted.get(b, 0) + 1
        
        for i in range(1, n + 1):
            if trusted.get(i, 0) == n - 1:
                return i
        
        return -1