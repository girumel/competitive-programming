class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        sum_freq = {0:1}
        
        prefix_sum = 0
        
        for i in range(n):
            prefix_sum += nums[i]
            
            if prefix_sum - k in sum_freq:
                count += sum_freq[prefix_sum - k]
            
            if prefix_sum in sum_freq:
                sum_freq[prefix_sum] += 1
            else:
                sum_freq[prefix_sum] = 1
        
        return count