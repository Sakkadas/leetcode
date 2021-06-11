"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
"""


class Solution:
    def reverse(self, x: int) -> int:
        res = int(str(abs(x))[::-1])
        if res.bit_length() > 31:
            return 0
        if x < 0:
            return -res
        else:
            return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(x=-321))
