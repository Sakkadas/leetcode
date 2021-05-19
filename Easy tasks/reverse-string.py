"""
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

"""


class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        rev_i = len(s) - 1
        while i < rev_i:
            s[i], s[rev_i] = s[rev_i], s[i]
            i += 1
            rev_i -= 1
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.reverseString(s=["h", "e", "l", "l", "o"]))
