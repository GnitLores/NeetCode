class Solution:
    # Return false if consecutive "Late" substring occurs
    # or if "Absent" char can be found twice.
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s: return False
        idx = s.find("A")
        if idx >= 0 and idx < len(s) - 1: # If "A" was found and it was not the final char
            if s[idx+1:].find("A") >= 0: # Look for second "A" following first
                return False
        return True

sol = Solution()
print(sol.checkRecord(s = "PPLLP"))
print(sol.checkRecord(s = "PPLLPA"))
print(sol.checkRecord(s = "PPLLPAA"))
print(sol.checkRecord(s = "PPALLP"))
print(sol.checkRecord(s = "PPALLPA"))
print(sol.checkRecord(s = "PPALLL"))