from typing import List


class Solution:
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