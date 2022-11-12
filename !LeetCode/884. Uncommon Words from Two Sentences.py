import collections
from itertools import count
from typing import List


class Solution:
    # Solution using counters.
    # Split the sentences and count words.
    # Check all words and see if count is one in one counter and
    # nonexistant in the other counter.
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count1 = collections.Counter(s1.split())
        count2 = collections.Counter(s2.split())
        res = []
        for w in count1.keys():
            if w not in count2 and count1[w] == 1:
                res.append(w)
        for w in count2.keys():
            if w not in count1 and count2[w] == 1:
                res.append(w)
        return res

sol = Solution()
print(sol.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
print(sol.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))