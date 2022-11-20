from typing import List


class Solution:
    # Unfold and zip to create columnwise iterables.
    # Compare each column to sorted version of itself to check if sorted.
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0 
        for col in zip(*strs):
            res += list(col) != sorted(col)
        return res
    
sol = Solution()
print(sol.minDeletionSize(strs = ["cba","daf","ghi"]))
print(sol.minDeletionSize(strs = ["a","b"]))
print(sol.minDeletionSize(strs = ["zyx","wvu","tsr"]))