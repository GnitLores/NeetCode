from typing import List
from collections import Counter

class Solution:
    # Use counter to check that count of characters is greater or equal than count
    # of characters in each word.
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0
        for w in words:
            wordCount = Counter(w)
            if all(count[c] >= wordCount[c] for c in w):
                res += len(w)
        return res

sol = Solution()
print(sol.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(sol.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))