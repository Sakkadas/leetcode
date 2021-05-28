"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return True if (int(num**0.5) ** 2) == num else False

if __name__ == "__main__":
    s = Solution()
    print(s.isPerfectSquare(14))