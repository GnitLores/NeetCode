from typing import List
from collections import Counter

class Solution:
    # You can find the intersection between two counters with the & operator.
    # The intersection is also a counter that contains only the elements contained
    # in both and the count is equal to the lowest count.
    # Consequently, if we find the intersection between counts for all words, we get
    # the count of letters that should be in the output. We just need to turn the count
    # into a list.
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])
        for i in range(1, len(words)):
            count = count & Counter(words[i])
            
        res = []
        for c in count.keys():
            res += [c] * count[c]
        return res

sol = Solution()
print(sol.commonChars(words = ["bella","label","roller"]))
print(sol.commonChars(words = ["cool","lock","cook"]))