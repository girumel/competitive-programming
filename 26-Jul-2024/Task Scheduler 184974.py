# Problem: Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        freq.sort()

        max_freq = freq[-1] - 1
        min_idle_time = max_freq * n

        for i in range(24, -1, -1):
            min_idle_time -= min(max_freq, freq[i])

        return len(tasks) + max(0, min_idle_time)