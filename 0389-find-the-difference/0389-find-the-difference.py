class Solution(object):
    def findTheDifference(self, s, t):
        for c in t:
            if c not in s or s.count(c) != t.count(c):
                return c
