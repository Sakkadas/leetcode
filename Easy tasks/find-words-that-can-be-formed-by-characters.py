"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
"""


class Solution:
    def countCharacters(self, words, chars: str) -> int:
        sum_chars = 0
        for word in words:
            flag = True
            for j in word:
                if word.count(j) > chars.count(j):
                    flag = False
            if flag:
                sum_chars += len(word)
        return sum_chars


if __name__ == "__main__":
    s = Solution()
    print(s.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
