# Problem: Score of parenthesis - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []

        for c in s:
            score = 0
            if c == '(':
                stack.append(c)
            else:
                while stack[-1] != '(':
                    score += stack.pop()
                stack.pop()
                if score == 0:
                    stack.append(1)
                else:
                    stack.append(2 * score)

        return score