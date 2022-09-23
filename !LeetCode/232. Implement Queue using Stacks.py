class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        self.queuify()
        return self.stack1.pop()

    def peek(self) -> int:
        self.queuify()
        return self.stack1[-1]
    
    def queuify(self) -> None: 
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def empty(self) -> bool:
        return (len(self.stack1) + len(self.stack2)) == 0

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

obj = MyQueue()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())

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