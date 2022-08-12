class MinStack:
    # With a stack, we know the order in which values will be removed.
    # Because of this, we can keep track of the minimum value by using a separate stack.
    # When pushing a value to the main stack, also push the current minimum value to separate stack.
    # All operations are O(1).
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