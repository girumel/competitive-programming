class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        
        max_div_score = 0
        max_div_indices = []
        
        i = 0
        while i < len(nums) + 1:
            div_score = i - prefix_sum[i] + prefix_sum[-1] - prefix_sum[i]
            
            if div_score > max_div_score:
                max_div_indices = [i]
                max_div_score = div_score
            elif div_score == max_div_score:
                max_div_indices.append(i)
                
            i += 1
        
        return max_div_indices
