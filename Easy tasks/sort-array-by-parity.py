"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums,
followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

"""


class Solution:
    def sortArrayByParity(self, nums):
        return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2 != 0]


if __name__ == '__main__':
    s = Solution()
    print(s.sortArrayByParity([3, 1, 2, 4]))
