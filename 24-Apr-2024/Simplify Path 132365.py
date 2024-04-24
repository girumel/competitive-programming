# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        names = path.split("/")
        canonical = "/"

        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
        canonical += "/".join(stack)
        
        return canonical