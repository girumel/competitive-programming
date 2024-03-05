class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = 0
        for j in range(len(s)):
            if i >= len(g):
                break
            if g[i] <= s[j]:
                i += 1
        
        return i
