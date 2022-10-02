class Solution:
    # Solution using state to count breakpoints.
    def countSegments(self, s: str) -> int:
        res = 0
        inSegment = False
        for c in s:
            if not inSegment:
                if c != " ":
                    inSegment = True
                    res += 1
            else:
                if c == " ":
                    inSegment = False
        return res
    
    # Solution counting breakpoints without using state.
    def countSegmentsNoState(self, s: str) -> int:
        if len(s) == 0: return 0
        res = int(s[0] != " ") # Count if first char is segment start
        for i in range(len(s) - 1):
            if s[i] == " " and s[i + 1] != " ":
                res += 1
        return res

    # Also very easily solved with built in function.
    def countSegmentsBuiltIn(self, s: str) -> int:
        return len(s.split())

sol = Solution()
print(sol.countSegments(s = "Hello, my name is John"))
print(sol.countSegments(s = "Hello"))
print(sol.countSegments(s = ""))
print(sol.countSegmentsNoState(s = "Hello, my name is John"))
print(sol.countSegmentsNoState(s = "Hello"))
print(sol.countSegmentsNoState(s = ""))
print(sol.countSegmentsBuiltIn(s = "Hello, my name is John"))
print(sol.countSegmentsBuiltIn(s = "Hello"))
print(sol.countSegmentsBuiltIn(s = ""))