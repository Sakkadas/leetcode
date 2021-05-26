"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

"""


class Solution:
    def maximumProduct(self, nums):
        x = sorted(nums)
        left = x[0] * x[1] * x[-1]
        right = x[-1] * x[-2] * x[-3]
        return max(left, right)


if __name__ == "__main__":
    s = Solution()
    print(s.maximumProduct([1, 2, 3, 4]))
