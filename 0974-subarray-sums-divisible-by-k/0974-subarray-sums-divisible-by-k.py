class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        count = [0] * k

        ps = [0] * (n + 1)

        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + nums[i - 1]

        for i in range(n + 1):
            count[ps[i] % k] += 1

        for i in range(k):
            result += count[i] * (count[i] - 1) // 2

        return result