# Problem: Left-and-right-sum-differences - https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        leftSum[0] = 0
        rightSum = [0] * n
        rightSum[n-1] = 0
        
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]

        answer = [abs(leftSum[i] - rightSum[i]) for i in range(n)]
        return answer