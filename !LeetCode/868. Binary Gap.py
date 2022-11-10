class Solution:
    # Convert to binary string and find indices of all 1s within string.
    # Find max difference between indices (0 if only one index exists).
    def binaryGap(self, n: int) -> int:
        idx = [i for i, b in enumerate(bin(n)[2:]) if b == "1"]
        maxGap = 0
        for i in range(1, len(idx)):
            maxGap = max(maxGap, idx[i] - idx[i - 1])
        return maxGap

sol = Solution()
print(sol.binaryGap(n = 22))
print(sol.binaryGap(n = 8))
print(sol.binaryGap(n = 5))