from typing import List


class Solution:
    # When I, add lowest number that has not yet been used
    # so that array must increase.
    # When D, add highest so it must decrease.
    # Add remaining value last.
    def diStringMatch(self, s: str) -> List[int]:
        lowDigit, highDigit = 0, len(s)
        res = []

        for c in s:
            res.append(lowDigit) if c == "I" else res.append(highDigit)
            if c == "I":
                lowDigit += 1
            else:
                highDigit -= 1
        res.append(lowDigit)
        return res

sol = Solution()
print(sol.diStringMatch(s = "IDID"))
print(sol.diStringMatch(s = "III"))
print(sol.diStringMatch(s = "DDI"))