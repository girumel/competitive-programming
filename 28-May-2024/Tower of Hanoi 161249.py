# Problem: Tower of Hanoi - https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1

class Solution:
    def toh(self, N, fromm, to, aux):
        if N == 1:
            print("move disk 1 from rod", fromm, "to rod", to)
            return 1
        else:
            count = self.toh(N-1, fromm, aux, to)
            print("move disk", N, "from rod", fromm, "to rod", to)
            count += 1
            count += self.toh(N-1, aux, to, fromm)
            return count