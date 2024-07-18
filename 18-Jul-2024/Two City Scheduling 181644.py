# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        
        costs.sort(key=lambda x: x[0] - x[1])
        
        for i in range(len(costs) // 2):
            min_cost += costs[i][0] + costs[i + len(costs) // 2][1]

        return min_cost