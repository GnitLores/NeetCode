class TimeMap:
    # Store in dictionary as a list of tuples (valu, timestamp).
    # Since timestamps are always increasing, we can insert by appending
    # in O(1) time and guarantee that the list is sorted by the timestamp.
    # This allows us to use binary search to get in O(logn) time.
    def __init__(self):
        self.timeStore = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeStore:
            self.timeStore[key] = []
        self.timeStore[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeStore.get(key, [])
        res = ""
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp: # Check if valid value
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
            
            

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)   # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1))   # return "bar"
print(timeMap.get("foo", 3))   # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4)  # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4))   # return "bar2"
print(timeMap.get("foo", 5))   # return "bar2"