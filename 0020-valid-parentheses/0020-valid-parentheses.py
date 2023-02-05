class Solution:
    def isValid(self, s: str) -> bool:
        opening = '({['
        closing = ')}]'
        stack = []
        for c in s:
            if c in opening:
                stack.append(c)
            elif c in closing:
                if len(stack) == 0:
                    return False
                if closing.index(c) != opening.index(stack.pop()):
                    return False
        return len(stack) == 0
                