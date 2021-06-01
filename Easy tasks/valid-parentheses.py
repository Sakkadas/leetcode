"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pseudo_stack = []
        bracket_dict = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for pr in s:
            if pr in bracket_dict.values():
                pseudo_stack.append(pr)
            else:
                if not pseudo_stack:
                    return False
                else:
                    if pseudo_stack[-1] == bracket_dict.get(pr):
                        del pseudo_stack[-1]
                    else:
                        return False

        return False if pseudo_stack else True


if __name__ == "__main__":
    s = Solution()
    print(s.isValid('()'))
