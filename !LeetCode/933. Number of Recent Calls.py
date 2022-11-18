from collections import deque

# Keep history of pings in queue. When pinging, pop all ping records that
# have expired before the given time limit before returning count.
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