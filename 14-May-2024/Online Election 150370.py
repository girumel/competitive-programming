# Problem: Online Election - https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leaders = {times[0]:persons[0]}
        self.times = times
        counts = {persons[0]:1}
        leader = persons[0]
        
        for i in range(1, len(persons)):
            counts[persons[i]] = counts.get(persons[i], 0) + 1
            if counts[persons[i]] >= counts.get(leader, 0):
                self.leaders[times[i]] = persons[i]
                leader = persons[i]
            else:
                self.leaders[times[i]] = leader
    
    def q(self, t: int) -> int:
        left, right = -1, len(self.times)

        while (left + 1) < right:
            mid = (left + right) // 2

            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
        
        return self.leaders[self.times[left]]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)