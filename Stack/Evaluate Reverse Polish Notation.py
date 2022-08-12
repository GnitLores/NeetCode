from typing import List
# Add number tokens to stack.
# Execute operation on top values of stack and add result to stack.
class Solution:
    def evalRPN(self, tokens: List):
        def add(x,y):
            return x + y
        def sub(x,y):
            return y - x
        def mult(x,y):
            return x * y
        def div(x,y):
            return int(y / x)

        opMap = {'+': add, '-': sub, '*': mult, '/': div}
        stack = []
        for tok in tokens:
            if tok in opMap.keys():
                stack.append(opMap[tok](stack.pop(), stack.pop()))
            else:
                stack.append(int(tok))

        return stack.pop()

def testSolution(*args):
    sol = Solution()
    res = sol.evalRPN(*args)
    print(res)

testSolution(["2","1","+","3","*"])
testSolution(["4","13","5","/","+"])
testSolution(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
