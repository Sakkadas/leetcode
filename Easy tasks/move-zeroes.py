"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""


class Solution:
    def moveZeroes(self, nums):
        itr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[itr], nums[i] = nums[i], nums[itr]
                itr += 1
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))
