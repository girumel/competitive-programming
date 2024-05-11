# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = (left + right) // 2

            total = 0
            for pile in piles:
                total += (pile + mid - 1) // mid

            if total <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left