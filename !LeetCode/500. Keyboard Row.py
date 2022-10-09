from typing import List


class Solution:
    # Create set of chars for each row, and convert each word to set of lower case chars.
    # Check if word set is subset of any row set.
    def findWords(self, words: List[str]) -> List[str]:
        row1 = {"q", "w", "e", "r", "t", "y", "u", "i", "o", "p"}
        row2 = {"a", "s", "d", "f", "g", "h", "j", "k", "l"}
        row3 = {"z", "x", "c", "v", "b", "n", "m"}

        def isRowSubset(w: str):
            w = set(w.lower())
            return w.issubset(row1) or w.issubset(row2) or w.issubset(row3)

        return [w for w in words if isRowSubset(w)]

sol = Solution()
print(sol.findWords(words = ["Hello","Alaska","Dad","Peace"]))
print(sol.findWords(words = ["omk"]))
print(sol.findWords(words = ["adsdf","sfd"]))