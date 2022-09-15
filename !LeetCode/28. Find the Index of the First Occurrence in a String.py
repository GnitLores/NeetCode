class Solution:
    # Semi-brute force solution.
    # Look for matches of first char in needle.
    # If match is found, search for subsequent chars of needle.
    # If all match, return index of first char.
    # In principle this is O(m*n) worst case, but in practice it
    # should usually be closer to O(n) because we do not match the entire
    # needle string. We only match subsequent characters if previous ones match.
    # It is very efficient when testing on leetcode.
    def strStrBruteForce(self, haystack: str, needle: str) -> int:
        for i, c in enumerate(haystack):
            if c == needle[0]:
                j = 0
                while i + j < len(haystack) and haystack[i + j] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                    j += 1
        return -1

sol = Solution()
print(sol.strStrBruteForce(haystack = "mississippi", needle = "sippi"))
print(sol.strStrBruteForce(haystack = "mississippi", needle = "issi"))
print(sol.strStrBruteForce(haystack = "sadbutsad", needle = "sad"))
print(sol.strStrBruteForce(haystack = "leetcode", needle = "leeto"))