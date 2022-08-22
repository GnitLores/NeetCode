class Solution:
    # Greedy solution.
    # Observation: if we iterate through closing as many pairs as possible and removing them,
    # only wildcards and unopened / unclosed parentheses will remain.
    # We can then iterate through again, first using wildcards to open unopened parentheses,
    # and then using wildcards to close unclosed parentheses.
    # If all remaining characters are wildcards, they can be turned into blanks, and the string
    # is valid.
    # O(n) time and very efficient on leetcode.
    def checkValidString(self, s: str) -> bool:
        s = [c for c in s]  # Turn string into list of chars.

        # Function that removes character pairs l and r when r is found.
        def removePairs(l, r, s):
            leftIdx = [] # i of left chars
            for i, c in enumerate(s):
                if c == l:
                    leftIdx.append(i)
                elif c == r: # if right char found, turn it and the last left char into "_"
                    if len(leftIdx) > 0:
                        s[leftIdx.pop()] = "_"
                        s[i] = "_"
            s = [c for c in s if c is not "_"] # remove all "_"
            return s

        s = removePairs("(", ")", s)
        s = removePairs("*", ")", s)
        s.reverse()
        s = removePairs("*", "(", s)

        s = [c for c in s if c is not "*"] # remove all remaining wildcards

        return len(s) == 0
    
    # Neetcode solution.
    # Use counters to track the range of possibilities in the count of unclosed parenthesis
    # to the left given the wildcard characters found.
    # Every wildcard character could be "(" adding one, ")" subtracting one, or " " doing nothing.
    # leftMin and leftMax is the min and max number of unclosed parenthesis.
    # If leftMax ever becomes negative, it means that we are forced to close a nonexisting "("
    # making the string invalid.
    # A negative number of unopened parentheses implies that we made an invalid choice for the
    # wild cards, so set it to a minimum of zero.
    # If at the end, leftMax was never negative, and leftMin is zero, the string is valid.
    # Also O(n) time.
    #
    # This is very elegant and clever but also unintuitive and hard to understand.
    # It also has the same complexity and runs quite a bit slower on leetcode.
    # Probably better just to stick to the first solution.
    def checkValidStringAlternative(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:  # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0
            

sol = Solution()
print(sol.checkValidString("()"))
print(sol.checkValidString("(*)"))
print(sol.checkValidString("(*))"))
print(sol.checkValidString("*)((*)))(*))(*"))
print(sol.checkValidString("*)((*))()(*))(*"))
print(sol.checkValidString(")*()*"))
print("")
print(sol.checkValidStringAlternative("()"))
print(sol.checkValidStringAlternative("(*)"))
print(sol.checkValidStringAlternative("(*))"))
print(sol.checkValidStringAlternative("*)((*)))(*))(*"))
print(sol.checkValidStringAlternative("*)((*))()(*))(*"))
print(sol.checkValidStringAlternative(")*()*"))