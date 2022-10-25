from typing import List


class Solution:
    # Stack solution.
    # Add integer scores to stack.
    # Operations work on top elements.
    # Finally, sum all scores.
    # O(n) time.
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            match o:
                case "+":
                    stack.append(stack[-1] + stack[-2])
                case "D":
                    stack.append(2 * stack[-1])
                case "C":
                    stack.pop()
                case other:
                    stack.append(int(o))
        return sum(stack)

sol = Solution()
print(sol.calPoints(operations = ["5","2","C","D","+"]))
print(sol.calPoints(operations = ["5","-2","4","C","D","9","+","+"]))
print(sol.calPoints(operations = ["1","C"]))
print(sol.calPoints(operations = []))