# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.tripMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInMap[id]
        del self.checkInMap[id]
        key = (startStation, stationName)
        if key not in self.tripMap:
            self.tripMap[key] = (0, 0)
        count, total = self.tripMap[key]
        self.tripMap[key] = (count + 1, total + t - startTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        count, total = self.tripMap[(startStation, endStation)]
        return total / count       


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)