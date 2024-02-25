class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        start = [0, 0]
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        
        my_distance = 0
        for i in range(2):
            d = abs(start[i] - target[i])
            my_distance += d
        
        min_ghost_distance = float('inf')
        for ghost in ghosts:
            ghost_distance = 0
            for i in range(2):
                d = abs(ghost[i] - target[i])
                ghost_distance += d
            min_ghost_distance = min(min_ghost_distance, ghost_distance)
        
        return my_distance < min_ghost_distance
    