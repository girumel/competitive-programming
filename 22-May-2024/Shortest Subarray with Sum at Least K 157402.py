# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        shortest = float('inf')
        queue = deque()
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = nums[i] + prefix_sum[i]

        for i in range(n + 1):
            while queue and prefix_sum[i] - prefix_sum[queue[0]] >= k:
                shortest = min(shortest, i - queue.popleft())
            
            while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
                queue.pop()

            queue.append(i)

        return shortest if shortest != float("inf") else -1