"""
Design the CombinationIterator class:

CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
next() Returns the next combination of length combinationLength in lexicographical order.
hasNext() Returns true if and only if there exists a next combination.

Example 1:
Input
["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[["abc", 2], [], [], [], [], [], []]
Output
[null, "ab", true, "ac", true, "bc", false]

Explanation
CombinationIterator itr = new CombinationIterator("abc", 2);
itr.next();    // return "ab"
itr.hasNext(); // return True
itr.next();    // return "ac"
itr.hasNext(); // return True
itr.next();    // return "bc"
itr.hasNext(); // return False
"""


import itertools


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.store = list(map(''.join, itertools.combinations(characters, combinationLength)))
        self.length_store = len(self.store)
        self.store = iter(self.store)
        self.count = 0

    def next(self) -> str:
        self.count += 1
        return next(self.store)

    def hasNext(self) -> bool:
        if self.count == self.length_store:
            return False
        else:
            return True


if __name__ == '__main__':
    obj = CombinationIterator('abc', 2)
    for i in range(3):
        print(obj.next())
        print(obj.hasNext())