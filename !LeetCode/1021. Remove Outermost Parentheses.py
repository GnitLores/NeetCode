class Solution:
    # Iterate through counting unclosed parenthesis amd adding chars to output.
    # If encountering a left paren results in there being 1 unclosed, this
    # is an outer paren and should not be added to the output.
    # If encountering a right paren results there being 0 unclosed, this is
    # also an outer paren that should not be added.
    def removeOuterParentheses(self, s: str) -> str:
        open, res = 0, []
        for c in s:
            if c == "(":
                open += 1
                if open > 1: res.append(c)
            else:
                open -= 1
                if open > 0: res.append(c)
        return "".join(res)

sol = Solution()
print(sol.removeOuterParentheses(s = "(()())(())"))
print(sol.removeOuterParentheses(s = "(()())(())(()(()))"))
print(sol.removeOuterParentheses(s = "()()"))