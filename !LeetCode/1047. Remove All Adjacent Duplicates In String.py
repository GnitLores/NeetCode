class Solution:
    # If we remove a pair of letters, we then need to check
    # the preceeding letter against the next letter as they are now adjacent.
    # Instead of repeatedly searching through the string, this can be naturally solved with a stack,
    # as the previous letter will be at the top of the stack after removing a pair.
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            stack.pop() if (stack and c == stack[-1]) else stack.append(c)
        return "".join(stack)

sol = Solution()
print(sol.removeDuplicates(s = "abbaca"))
print(sol.removeDuplicates(s = "azxxzy"))
print(sol.removeDuplicates(s = "aaaaaaaaa"))