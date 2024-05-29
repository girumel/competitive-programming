# Problem: Find in Mountain Array - https://leetcode.com/problems/find-in-mountain-array/description/

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        n = mountain_arr.length()

        # find the peak of the mountain
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                l = mid + 1
            else:
                r = mid
        peak = l

        # search for the target in the ascending part
        l, r = 0, peak
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        
        # search for the target in the descending part
        l, r = peak, n-1
        while l < r:
            mid = (l + r) // 2
            if mountain_arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid
        if mountain_arr.get(l) == target:
            return l
        
        return -1