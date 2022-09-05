import collections


class Solution:
    # Count using dictionary and return first letter with count 1.
    def firstUniqChar(self, s: str) -> int:
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1: return i
        return -1

sol = Solution()
print(sol.firstUniqChar("leetcode"))
print(sol.firstUniqChar("loveleetcode"))
print(sol.firstUniqChar("aabb"))