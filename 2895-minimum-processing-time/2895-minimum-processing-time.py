class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        max_time = 0
        tasks.sort(reverse=True)
        processorTime.sort()
        
        i = 0
        for pt in processorTime:
            if i < len(tasks):
                time_taken = max([pt+task for task in tasks[i:i+4]])
                max_time = max(max_time, time_taken)
                i += 4
        return max_time