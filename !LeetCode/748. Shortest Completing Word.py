from collections import Counter
from typing import List


class Solution:
    # We can count the letters and compare letter counts to find valid words.
    # A convenient way to do this is with the a counter.
    # Using the & operator on two counters gives the intersection, that is
    # it returns a counter with the letters contained in both and the lowest count.
    # Ex:
    # D1 = Counter({'A': 2, 'B': 1, 'C': 4, 'D': 5})
    # D2 = Counter({'A': 3, 'B': 4, 'C': 4, 'D': 7})
    # D1 & D2 = Counter({'D': 5, 'C': 4, 'A': 2, 'B': 1})
    #
    # This means that we can check if word w is a completing word by checking if
    # the plate counter is equal to the intersection of the plate counter and the word counter.
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plateCount = Counter([c.lower() for c in licensePlate if c.isalpha()])
        shortest = None
        for w in words:
            if plateCount & Counter(w) == plateCount:
                if not shortest or len(w) < len(shortest):
                    shortest = w
        return shortest

sol = Solution()
print(sol.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
print(sol.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))