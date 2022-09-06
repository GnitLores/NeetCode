from typing import List


class Solution:
    # Two pointer solution.
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return

sol = Solution()
sol.reverseString(["h","e","l","l","o"])
sol.reverseString(["H","a","n","n","a","h"])