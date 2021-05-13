class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        results = []
        for i in candies:
            if (i + extraCandies) < max(candies):
                results.append(False)
            else:
                results.append(True)

        return results
