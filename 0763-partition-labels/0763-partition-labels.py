class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_to_last_index = {c: i for i, c in enumerate(s)}
        start, end = 0, 0
        partition_sizes = []

        for index, char in enumerate(s):
            end = max(end, char_to_last_index[char])
            if index == end:
                partition_sizes.append(end - start + 1)
                start = index + 1

        return partition_sizes