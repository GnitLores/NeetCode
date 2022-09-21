import collections
# Solution using two queues.
# Queue 1 acts as the stack, and queue 2 is used to push elements to it.
# When pushing:
# - Push the new element to queue 2.
# - Pop all elements from queue 1 to queue 2.
# - swap the pointers between queue 1 and queue 2.
# This results in the new element being at the head of queue 1.
class MyStackDoubleQueue:
    def __init__(self):
        self.q1 = collections.deque()
        self.q2 = collections.deque()
    
    def push(self, x: int) -> None:
        if not x: return
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
            
    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

obj = MyStackDoubleQueue()
print(obj.empty())
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
print(obj.pop())
print(obj.pop())
obj.push(6)
pass
