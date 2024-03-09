class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad_ints = set()
        
        for i, v in enumerate(fronts):
            if v == backs[i]:
                bad_ints.add(v)
            
        good_ints = set(fronts + backs) - bad_ints
        
        return min(good_ints) if len(good_ints) != 0 else 0