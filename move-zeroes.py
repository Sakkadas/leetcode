class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        itr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[itr], nums[i] = nums[i], nums[itr]
                itr += 1
        return nums
