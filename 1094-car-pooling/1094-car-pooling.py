class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        location = []

        for trip in trips:
            location.append((trip[1], trip[0]))
            location.append((trip[2], -trip[0]))
        location.sort()

        for time, passengers in location:
            capacity -= passengers
            if capacity < 0:
                return False

        return True