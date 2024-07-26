# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        max_freq = max(freq.values())
        max_freq_tasks = 0
        for task in freq:
            if freq[task] == max_freq:
                max_freq_tasks += 1
                
        min_idle_time = (max_freq - 1) * (n + 1)
        min_idle_time += max_freq_tasks
        
        return max(min_idle_time, len(tasks))