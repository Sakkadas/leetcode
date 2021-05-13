class Solution:
    def intToRoman(self, num: int) -> str:
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
        result = []
        for i in range(len(ints)):
            count = int(num / ints[i])
            result.append(nums[i] * count)
            num -= ints[i] * count
        return ''.join(result)
