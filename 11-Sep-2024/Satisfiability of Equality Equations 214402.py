# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_x] = root_y

        for equation in equations:
            if equation[1] == "=":
                x = ord(equation[0]) - ord("a")
                y = ord(equation[3]) - ord("a")
                union(x, y)
                
        for equation in equations:
            if equation[1] == "!":
                x = ord(equation[0]) - ord("a")
                y = ord(equation[3]) - ord("a")
                if find(x) == find(y):
                    return False
        return True