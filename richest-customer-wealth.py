class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in range(len(accounts)):
            if richest < sum(accounts[i]):
                richest = sum(accounts[i])

