class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set(match[0] for match in matches)
        losers = set(match[1] for match in matches)
        
        unique_winners = sorted(list(winners - losers))
        
        losers_dict = {}
        for match in matches:
            if match[1] in losers_dict:
                losers_dict[match[1]] += 1
            else:
                losers_dict[match[1]] = 1
                
        unique_losers = sorted([loser for loser in losers_dict if losers_dict[loser] == 1])
        
        return [unique_winners, unique_losers]
