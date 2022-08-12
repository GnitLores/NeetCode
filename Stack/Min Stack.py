class MinStack:

    def __init__(self):
        self.stack = []
        self.minVals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minVals:
            self.minVals.append(val)
        else:
            self.minVals.append(min(val, self.minVals[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minVals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVals[-1]

s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())
s.pop()
print(s.top())
print(s.getMin())