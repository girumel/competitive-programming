class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pair_sums = []
        i, j = 0, len(nums)- 1
        
        while i < j:
            pair_sums.append(nums[i] + nums[j])
            i += 1
            j -= 1
        
        return max(pair_sums)