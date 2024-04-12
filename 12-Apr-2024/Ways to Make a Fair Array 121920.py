# Problem: Ways to Make a Fair Array - https://leetcode.com/problems/ways-to-make-a-fair-array/description/

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        odd_sum = [0] * (n + 1)
        even_sum = [0] * (n + 1)

        for i in range(n):
            odd_sum[i + 1] = odd_sum[i]
            even_sum[i + 1] = even_sum[i]

            if i % 2 == 0:
                even_sum[i + 1] += nums[i]
            else:
                odd_sum[i + 1] += nums[i]

        for i in range(n):
            odd_indexed = odd_sum[i] + even_sum[n] - even_sum[i + 1]
            even_indexed = even_sum[i] + odd_sum[n] - odd_sum[i + 1]
            if odd_indexed == even_indexed:
                count += 1

        return count