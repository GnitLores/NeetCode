class Solution:
    # If we have a pair of consecutive groups of 1s and 0s,
    # the number of possible substrings with an equal number of 
    # 1s and 0s is the minimum of the number of each.
    # For example, the string "1110000" has 3 ones and 4 zeros
    # and min(3, 4) = 3 valid substrings - "10", "1100", and "111000".
    #
    # We can start by counting the length of all the consecutive groups,
    # and then iterate through pairs of adjacent groups and find the min of each pair.
    # The sum of these mins is the total number of valid substrings.
    # O(n) time.
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        count = 0
        for i in range(len(s)):
            count += 1
            if i == len(s) - 1 or s[i] != s[i + 1]:
                counts.append(count)
                count = 0
        res = 0
        for i in range(len(counts) - 1):
            res += min(counts[i], counts[i + 1])

        return res

sol = Solution()
print(sol.countBinarySubstrings(s = "00110011"))
print(sol.countBinarySubstrings(s = "10101"))