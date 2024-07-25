# Problem: Smallest Number in Infinite Set - https://leetcode.com/problems/smallest-number-in-infinite-set/description/

class SmallestInfiniteSet:

    def __init__(self):
        self.count = 1
        self.heap = []

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.count += 1
        return self.count - 1

    def addBack(self, num: int) -> None:
        if num not in self.heap and num < self.count:
            heapq.heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)