# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(dg1, dg2):
            if dg1 + dg2 > dg2 + dg1:
                return -1
            elif dg1 + dg2 < dg2 + dg1:
                return 1
            else:
                return 0
    
        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        ans = ''.join(nums)
        return '0' if ans[0] == '0' else ans