# Problem: Maximum Points You Can Obtain from Cards - https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + cardPoints[i]

        max_score = 0
        for i in range(k + 1):
            max_score = max(max_score, prefix_sum[i] + prefix_sum[n] - prefix_sum[n - k + i])

        return max_score