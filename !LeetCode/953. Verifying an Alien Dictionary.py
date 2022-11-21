import string
from typing import List


class Solution:
    # - Create a dictionary mapping alien letters to lowercase english letters.
    # - Translate list of words to english letters using dictionary.
    # - Compare list to sorted list.
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashmap = dict(zip(order, list(string.ascii_lowercase)))
        words = ["".join([hashmap[c] for c in w]) for w in words]
        return words == sorted(words)
    
sol = Solution()
print(sol.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"))
print(sol.isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
print(sol.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"))