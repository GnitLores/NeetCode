class Solution(object):
    # Backtracking solution.
    # Should be O(2^n) time.
    def generateParenthesis(self, n):
        res = []
        
        def findParenthesis(str, nOpen, nClose):
            if nClose > nOpen:
                return

            if nOpen == n and nClose == n:
                res.append(str)

            if nOpen < n:
                findParenthesis("".join([str, '(']), nOpen + 1, nClose)
            
            if nClose < n:
                findParenthesis("".join([str, ')']), nOpen, nClose + 1)

        findParenthesis('', 0, 0)
        
        return res

    # Could also have been implemented with a stack.
    # Prevents string concatenation but requires a few more lines of codes.
    # Does not seem more efficient.
    def generateParenthesisStack(self, n):
        res = []
        stack = []
        
        def findParenthesis(nOpen, nClose):
            if nClose > nOpen:
                return

            if nOpen == n and nClose == n:
                res.append("".join(stack))

            if nOpen < n:
                stack.append('(')
                findParenthesis(nOpen + 1, nClose)
                stack.pop()
            
            if nClose < n:
                stack.append(')')
                findParenthesis(nOpen, nClose + 1)
                stack.pop()

        findParenthesis(0, 0)
        
        return res

sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesisStack(3))