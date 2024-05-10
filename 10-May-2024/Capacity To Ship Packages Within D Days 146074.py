# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            ship_weight = 0
            day = 1
            for weight in weights:
                if ship_weight + weight > mid:
                    day += 1
                    ship_weight = 0
                ship_weight += weight
            
            if day <= days:
                right = mid
            else:
                left = mid + 1
        
        return left