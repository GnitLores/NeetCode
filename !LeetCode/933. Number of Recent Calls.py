from collections import deque

# Keep hisotory of pings in queue and when pinging
# pop all pings that have expired before returning count.
class RecentCounter:

    def __init__(self):
        self.q = deque()
        return

    def ping(self, t: int) -> int:
        self.q.append(t)
        limit = t - 3000
        while self.q and self.q[0] < limit:
            self.q.popleft()
        return len(self.q)
        

obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)