class MyQueueSimple:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(x)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0

print("")
obj = MyQueueSimple()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())