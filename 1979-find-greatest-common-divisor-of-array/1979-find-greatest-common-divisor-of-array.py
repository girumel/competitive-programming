class Solution:
    def findGCD(self, nums: List[int]) -> int:
        gcd = 1
        sml = min(nums)
        lrg = max(nums)
        if sml == lrg:
            gcd = sml
        else:
            for i in range(2, sml + 1):
                if sml % i == 0 and lrg % i == 0:
                    gcd = i
        return gcd
    