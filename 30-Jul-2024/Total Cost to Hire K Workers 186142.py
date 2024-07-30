# Problem: Total Cost to Hire K Workers - https://leetcode.com/problems/total-cost-to-hire-k-workers/description/

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        workers = []
        
        for i in range(n):
            workers.append((costs[i], i))
        workers.sort()
        
        heap = []
        heapq.heapify(heap)
        total_cost = 0
        
        for i in range(k):
            if i < candidates:
                heapq.heappush(heap, -workers[i][0])
                total_cost += workers[i][0]
            else:
                heapq.heappush(heap, -workers[i][0])
                total_cost += workers[i][0]
                total_cost += heapq.heappop(heap)
                
        return total_cost