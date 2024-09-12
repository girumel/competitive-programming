# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def most_k(nums, k):
            count = collections.Counter()
            left = res = 0
            for right, num in enumerate(nums):
                if count[num] == 0:
                    k -= 1
                count[num] += 1
                while k < 0:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        k += 1
                    left += 1
                res += right - left + 1
            return res
        
        return most_k(nums, k) - most_k(nums, k - 1)