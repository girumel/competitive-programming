# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        for i in range(len(quality)):
            workers.append((quality[i], wage[i]))
        workers.sort(key = lambda w: w[1] / w[0])

        heap = []
        heapq.heapify(heap)
        total_quality = 0
        least_money = float('inf')

        for quality, wage in workers:
            total_quality += quality
            heapq.heappush(heap, -quality)

            if len(heap) > k:
                total_quality += heapq.heappop(heap)
            
            if len(heap) == k:
                least_money = min(least_money, total_quality * (wage/quality))

        return least_money