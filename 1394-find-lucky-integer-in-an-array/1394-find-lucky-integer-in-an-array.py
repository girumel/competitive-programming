class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}
        lucky = 0
        for n in arr:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        for n in hashmap:
            if hashmap[n] == n:
                lucky = max(lucky, n)

        if lucky == 0:
            return -1
        else:
            return lucky
        