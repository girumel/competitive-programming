class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = set(list1) & set(list2)
        index_sums = {string: (list1.index(string) + list2.index(string)) for string in common_strings}
        min_index_sum = min(index_sums.values())
        return [string for string, index_sum in index_sums.items() if index_sum == min_index_sum]
