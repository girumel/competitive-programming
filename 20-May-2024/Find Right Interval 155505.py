# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        result = [-1] * n

        sorted_intervals = []
        for index, (start, _) in enumerate(intervals):
            sorted_intervals.append((start, index))
        sorted_intervals.sort()

        for index, (_, end) in enumerate(intervals):
            left, right = 0, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if sorted_intervals[mid][0] >= end:
                    result[index] = sorted_intervals[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
        
        return result