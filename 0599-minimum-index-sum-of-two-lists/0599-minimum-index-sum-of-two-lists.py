class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings_with_index_sums = {string: (list1.index(string) + list2.index(string)) for string in list(set(list1) & set(list2))}
        return [string for string, index_sum in common_strings_with_index_sums.items() if index_sum == min(common_strings_with_index_sums.values())]
            