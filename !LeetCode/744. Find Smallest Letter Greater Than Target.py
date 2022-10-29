from typing import List


class Solution:
    # The only tricky part about this problem is the boundary condition for the last letter.
    # If the last letter is not lexographically greater, than the first letter must be returned.
    # Once this check is made, the problem is extremely simple.
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target: return letters[0]

        for c in letters:
            if target < c: return c

sol = Solution()
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))
print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "j"))