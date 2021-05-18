"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1
"""

from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        quantity = 0
        for i in range(1, len(tiles) + 1):
            for j in set(permutations(tiles, i)):
                quantity += 1
        return quantity


if __name__ == "__main__":
    s = Solution()
    print(s.numTilePossibilities('AAABBC'))
