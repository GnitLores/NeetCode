from typing import List


class Solution:
    # Use zip on the unpacked list of strings gives a list of tuples
    # with each tuple containing the ith char of that string.
    # Check if all chars are the same.
    # Zip stops with the shortest input, so we don't have to check for that.
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for group in zip(*strs):
            if all(x == group[0] for x in group):
                res.append(group[0])
            else:
                break
        return "".join(res)

sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))