"""
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the ith
customer has in the j bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts.
The richest customer is the customer that has the maximum wealth.
"""


class Solution:
    def maximumWealth(self, accounts):
        richest = 0
        for i in range(len(accounts)):
            if richest < sum(accounts[i]):
                richest = sum(accounts[i])
        return richest


if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1, 2, 3], [3, 2, 1]]))
