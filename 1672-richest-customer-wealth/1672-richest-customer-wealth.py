class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0;
        for i in range(len(accounts)):
            total = sum(accounts[i])
            if total > max:
                max = total
        return max
        