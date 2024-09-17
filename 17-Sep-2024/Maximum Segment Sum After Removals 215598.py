# Problem: Maximum Segment Sum After Removals - https://leetcode.com/problems/maximum-segment-sum-after-removals/description/

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        parent = list(range(n))
        answer = [0] * n

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            parent[root_x] = root_y
            segment_sum[root_y] += segment_sum[root_x]

        segment_sum = [0] * n
        max_sum = 0

        for j in range(n - 1, 0, -1):
            i = removeQueries[j]
            segment_sum[i] = nums[i]
          
            if i > 0 and segment_sum[find(i - 1)]:
                union(i, i - 1)
            if i < n - 1 and segment_sum[find(i + 1)]:
                union(i, i + 1)

            max_sum = max(max_sum, segment_sum[find(i)])
            answer[j - 1] = max_sum

        return answer