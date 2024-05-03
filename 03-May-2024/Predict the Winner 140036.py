# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def max_score(nums, i, j):
            if i == j:
                return nums[i]
            return max(nums[i] - max_score(nums, i+1, j), nums[j] - max_score(nums, i, j-1))
        
        return max_score(nums, 0, len(nums)-1) >= 0