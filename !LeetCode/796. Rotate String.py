import collections


class Solution:
    # Linear time solution.
    # Algorithmically more efficient than the other solution
    # but much more complicated.
    # Check that length is equal and that char counts are equal.
    # Use sliding window technique to identify the segment starting
    # the string s in string goal.
    # Check if that segment ends string goal, and if the remainder of
    # string s equals string goal.
    # If so, s can be rotated to become goal.
    def rotateStringLinear(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if collections.Counter(s) != collections.Counter(goal): return False

        maxWin = 0
        start = 0
        while start < len(s):
            while start < len(s) and s[0] != goal[start]:
                start += 1
            win = 0
            while start + win < len(s) and goal[start + win] == s[win]:
                win += 1
                if win > maxWin:
                    winStart = start
                    maxWin = win
            win = 0
            start += 1
        
        if winStart + maxWin != len(s): return False
        if s[maxWin:] == goal[0:len(s) - maxWin]: return True
        return False

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
print(sol.rotateStringLinear(s = "gcmbf", goal = "fgcmb"))
print(sol.rotateStringLinear(s = "abcde", goal = "cdeab"))
print(sol.rotateStringLinear(s = "abcde", goal = "abced"))
print("")
print(sol.rotateString(s = "gcmbf", goal = "fgcmb"))
print(sol.rotateString(s = "abcde", goal = "cdeab"))
print(sol.rotateString(s = "abcde", goal = "abced"))