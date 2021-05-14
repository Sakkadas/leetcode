class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums) + 1):
            res.append(sum(nums[0:i]))
        return(res)