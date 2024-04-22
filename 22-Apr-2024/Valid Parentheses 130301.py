# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        mappings =  {"(": ")", "[": "]",  "{": "}"}
        openings = set(["(", "[", "{"])
        stack = []
        
        for c in s:
            if c in openings:
                stack.append(c)
            elif stack and c == mappings[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0
                