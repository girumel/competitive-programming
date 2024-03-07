class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams = []
        left, right = 0, len(skill) - 1
        total_skill = skill[left] + skill[right]
        while left < right:
            if skill[left] + skill[right] != total_skill:
                return -1
            teams.append((skill[left], skill[right]))
            left, right = left + 1, right - 1
        
        sum_of_skill_products = 0
        for team in teams:
            sum_of_skill_products += team[0] * team[1]
        return sum_of_skill_products