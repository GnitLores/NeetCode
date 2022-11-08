class Solution:
    # Add characters to a stack and pop from the stack when encountering a backspace
    # as long as the stack is not empty.
    # Join result into new string and compare.
    # It is not actually necessary to turn the stacks back into strings, but
    # it is faster when testing on leetcode.
    def backspaceCompare(self, s: str, t: str) -> bool:
        def processText(text):
            stack = []
            for c in text:
                if c == "#":
                    if len(stack) > 0: stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
            
        return processText(s) == processText(t)

sol = Solution()
print(sol.backspaceCompare(s = "ab#c", t = "ad#c"))
print(sol.backspaceCompare(s = "ab##", t = "c#d#"))
print(sol.backspaceCompare(s = "a#c", t = "b"))