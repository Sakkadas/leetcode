class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        temlate = [s for s in jewels]
        for i in stones:
            if i in temlate:
                result += 1
        return result