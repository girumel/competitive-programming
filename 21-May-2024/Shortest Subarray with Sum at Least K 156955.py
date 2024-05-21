# Problem: Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        queue = deque([(-1, 0)])
        running_sum = 0
        shortest = float('inf')

        for i in range(n):
            running_sum += nums[i]

            while queue and running_sum <= queue[-1][1]:
                queue.pop()
            
            queue.append((i, running_sum))

            while queue and running_sum - queue[0][1] >= k:
                shortest = min(shortest, i - queue.popleft()[0])

        return shortest if shortest != float("inf") else -1