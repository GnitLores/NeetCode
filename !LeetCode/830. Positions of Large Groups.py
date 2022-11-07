class Solution:
    # Deal with edge conditions before and after loop.
    # Every element other than the first and last can be handled in the same way
    # in the loop.
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        if len(s) < 3: return []

        start, char, res = 0, s[0], []
        for i in range(1, len(s)):
            if s[i] != char:
                if (i - start) >= 3: res.append([start, i - 1])
                start = i
                char = s[i]
        if (len(s) - start) >= 3: res.append([start, len(s) - 1])

        return res

sol = Solution()
print(sol.largeGroupPositions(s = "abbxxxxzzy"))
print(sol.largeGroupPositions(s = "abc"))
print(sol.largeGroupPositions(s = "abcdddeeeeaabbbcd"))