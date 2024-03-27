class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0

        p = 0
        t = 0
        
        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                matches += 1
                p += 1
                t += 1
            else:
                t += 1
        
        return matches