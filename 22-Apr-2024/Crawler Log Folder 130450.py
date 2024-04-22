# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        min_ops = 0

        for log in logs:
            if log == "../":
                min_ops = max(0, min_ops-1)
            elif log == "./":
                continue
            else:
                min_ops += 1

        return min_ops