"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: c = 3
Output: false

Example 3:
Input: c = 4
Output: true

Example 4:
Input: c = 2
Output: true

Example 5:
Input: c = 1
Output: true

"""

import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True

        for i in range(1, int(math.sqrt(c) + 1)):
            j = c - i ** 2
            if int(math.sqrt(j)) ** 2 == j:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.judgeSquareSum(5))
