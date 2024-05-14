# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        min_radius = 0
        
        for house in houses:
            left, right = 0, len(heaters) - 1
            radius = float('inf')
            
            while left <= right:
                mid = (left + right) // 2
                heat = heaters[mid]
                radius = min(radius, abs(heat - house))
                
                if house < heat:
                    right = mid - 1
                elif house > heat:
                    left = mid + 1
                else:
                    break
            
            min_radius = max(min_radius, radius)
            
        return min_radius