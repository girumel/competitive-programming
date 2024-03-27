class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0
        
        for player in players:
            for trainer in trainers:
                if player <= trainer:
                    matches += 1
                    trainers.remove(trainer)
                    break
        
        return matches