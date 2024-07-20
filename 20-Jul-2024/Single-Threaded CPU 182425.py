# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        sorted_tasks = []
        for i, task in enumerate(tasks):
            sorted_tasks.append((task[0], task[1], i))
        sorted_tasks.sort()
        
        heap = []
        heapq.heapify(heap)

        time = 0
        order = []

        i = 0        
        while i < n or heap:
            if not heap:
                time = max(time, sorted_tasks[i][0])
            while i < n and sorted_tasks[i][0] <= time:
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i += 1
            duration, idx = heapq.heappop(heap)
            time += duration
            order.append(idx)
            
        return order