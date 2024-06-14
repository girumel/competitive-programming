# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(index, sequence):
            if len(sequence) > 2 and index == len(num):
                return True

            for i in range(index, len(num)):
                current = num[index:i+1]

                if current[0] == '0' and len(current) != 1:
                    continue

                if len(sequence) >= 2:
                    prev_two_sum = int(sequence[-1]) + int(sequence[-2])

                    if int(current) > prev_two_sum:
                        break

                    if int(current) == prev_two_sum:
                        if backtrack(i+1, sequence + [current]):
                            return True

                elif backtrack(i+1, sequence + [current]):
                    return True

            return False

        return backtrack(0, [])