class Solution(object):
    # Create a hashmap to associate closing and opening parenthesis of the same type.
    # Add opening parenthesis to a stack.
    # Compare closing parenthesis to the top element of the stack.
    # If there is a mismatch, return false.
    # If it matches, pop from the stack and continue.
    # O(n) time and faster than 87.7% of solutions.
    def isValid(self, s):
        if (len(s) % 2) == 1: # The input string must be even in length to be valid
            return False
        
        parenMap = {')':'(', ']':'[', '}':'{',}
        parenStack = []
        for c in s:
            if c in parenMap:
                if len(parenStack) > 0 and parenStack[-1] == parenMap[c]:
                    parenStack.pop()
                else:
                    return False
            else:
                parenStack.append(c)

        if len(parenStack) > 0:
            return False
        else:
            return True


def testSolution(*args):
    sol = Solution
    result = sol.isValid(sol, *args)
    print(": " + str(result))

testSolution("()")
testSolution("()[]{}")
testSolution("(]")
testSolution("((")
testSolution("(")
testSolution("")
testSolution("){")
testSolution("([)]")