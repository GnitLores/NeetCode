from typing import List


class Solution:
    # Split strings on spaces and iterate through words except for the last two words.
    # If we find first, check if next is second, and if so add next after that to output.
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        res = []
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                res.append(text[i + 2])
        return res

sol = Solution()
print(sol.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))
print(sol.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))