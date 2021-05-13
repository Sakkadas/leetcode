class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            lower = [j for j in nums if i > j]
            res.append(len(lower))
        return res