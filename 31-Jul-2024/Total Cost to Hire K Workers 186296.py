# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        left, right = 0, len(costs) - 1
        count = 0
        total_cost = 0
        
        while left <= right and count < candidates:
            heapq.heappush(heap, (costs[left], 'l'))
            if left != right:
                heapq.heappush(heap, (costs[right], 'r'))
            left += 1
            right -= 1
            count += 1
        
        for _ in range(k):
            cost, direction = heapq.heappop(heap)
            total_cost += cost
            if direction == 'l':
                if left <= right:
                    heapq.heappush(heap, (costs[left], 'l'))
                    left += 1
            else:
                if left <= right:
                    heapq.heappush(heap, (costs[right], 'r'))
                    right -= 1
        
        return total_cost