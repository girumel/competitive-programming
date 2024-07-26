# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_freq = max(freq.values())
        max_freq_tasks = 0
        min_idle_time = (max_freq - 1) * (n + 1)
        for key in freq:
            if freq[key] == max_freq:
                max_freq_tasks += 1

        min_idle_time += max_freq_tasks
        return max(min_idle_time, len(tasks))