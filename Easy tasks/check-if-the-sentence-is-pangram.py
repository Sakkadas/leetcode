from string import ascii_lowercase,ascii_uppercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if set(sentence) == set(ascii_lowercase) or set(sentence) == set(ascii_uppercase):
            return True
        else:
            return False
