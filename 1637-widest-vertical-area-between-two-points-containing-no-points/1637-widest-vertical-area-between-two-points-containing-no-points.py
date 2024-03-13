class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = 0
        left, right = 0, 1
        
        while left < right and right < len(points):
            max_width = max(max_width, points[right][0] - points[left][0])
            left += 1
            right += 1
        
        return max_width