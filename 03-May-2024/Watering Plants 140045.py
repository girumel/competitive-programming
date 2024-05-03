# Problem: Watering Plants - https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity
        for i, plant in enumerate(plants):
            if water < plant:
                steps += 2 * i
                water = capacity
            water -= plant
        
        return steps + len(plants)