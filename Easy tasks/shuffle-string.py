class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        itr = 0
        letters_with_indxs = {}
        result = ''
        while len(s) > itr:
            letters_with_indxs[indices[itr]] = s[itr]
            itr += 1
        for i in sorted(letters_with_indxs):
            result += letters_with_indxs[i]
        return result
