# Problem: Evaluate Reverse Polish Notation - https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                int2 = stack.pop()
                int1 = stack.pop()
                if token == '+':
                    stack.append(int1 + int2)
                elif token == '-':
                    stack.append(int1 - int2)
                elif token == '*':
                    stack.append(int1 * int2)
                else:
                    stack.append(int(float(int1 / int2)))
            else:
                stack.append(int(token))

        return stack[0]