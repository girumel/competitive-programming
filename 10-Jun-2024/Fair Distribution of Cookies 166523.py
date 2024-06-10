# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        min_unfairness = float("inf")

        def backtrack(start, children):
            nonlocal min_unfairness

            if start == n:
                min_unfairness = min(min_unfairness, max(children))
                return

            for i in range(k):
                children[i] += cookies[start]
                backtrack(start + 1, children)
                children[i] -= cookies[start]

                if children[i] == 0:
                    break

        backtrack(0, [0] * k)
        return min_unfairness