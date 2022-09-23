class MyQueue:
    # We can pop all elements from one stack and append to the other
    # which reverses the order and turns a FILO structure into a FIFO structure.
    # This means that it is easy to turn a stack into a queue.
    # The problem is that pushing is slow,since we need to queify the entire
    # structure every time we push a value.
    # 
    # A solution is to keep one stack queified and push new values to the other stack.
    # Only once the queuified stack is empty do we add whatever is in the other stack to it.
    # This works since the oldest values always leave first in a FIFO structure.
    # This makes pushing O(1) since we just append to the secondary stack.
    # Since we need to queuify the entire secondary stack whenever the primary stack becomes empty,
    # popping and peeping beomce worst case O(n) operations.
    # However, this only has to happen once for each value, once it is done it is never repeated.
    # So overall the run time of pop and peep are amortized O(1).
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
    
    # WHen the primary stack is empty, reverse the order of everything
    # stored up in the secondary stack and move it to the primary.
    def queuify(self) -> None: 
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

    def empty(self) -> bool:
        return (len(self.stack1) + len(self.stack2)) == 0

# Simple solution.
# Stack1 acts as the queue.
# Every time we push a new value, pop everuthing in stack1 and append to stack 2.
# This reverses the order.
# Append the new value to stack2.
# Pop everything from stack2 to stack1, reversing the order again.
# This results in stack1 being first in first out.
# However, pushing is a O(n) operation.
# All other operations are O(1).
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