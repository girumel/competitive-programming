class Solution:
    def totalFruit(self, fruits: List[int]) -> int:    
        n = len(fruits)
        baskets = {}
        longest = 0
        left = 0

        for right in range(n):
            baskets[fruits[right]] = right

            if len(baskets) > 2:
                min_index = min(baskets.values())
                del baskets[fruits[min_index]]
                left = min_index + 1

            longest = max(longest, right - left + 1)

        return longest