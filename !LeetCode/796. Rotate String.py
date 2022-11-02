import collections


class Solution:
    # O(n^2) time slution.
    # Rotating the string as many times as there are
    # characters in it gices the string itself.
    # Thus, we want to rotate a max of len - 1 times.
    # For each step of the rotation, check if the string
    # is equal to target.
    # This is an O(n^2) speed operation, so checking if the
    # letter counts are equal first offers a moderate performance increase
    # since that can be done in O(n) time and deals with many possible inputs.
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if collections.Counter(s) != collections.Counter(goal): return False
        rotations = len(s) - 1
        while rotations > 0:
            s = "".join([s[1:], s[0]])
            rotations -= 1
            if s == goal: return True
        return False

sol = Solution()
print(sol.rotateString(s = "gcmbf", goal = "fgcmb"))
print(sol.rotateString(s = "abcde", goal = "cdeab"))
print(sol.rotateString(s = "abcde", goal = "abced"))