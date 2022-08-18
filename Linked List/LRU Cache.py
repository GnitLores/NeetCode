# Solution using dictionary and doubly linked list.
# Entries in the dictionary are nodes of the linked list.
# Left most entries in list are LRU and rightmost entries are MRU.
# Using a left and right dummy node on either end simplifies operations.
# O(1) time to put and get.

class LRUNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.val = val
        self.key = key # We need to include the key in the rntry for removing entries from dictionary
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        # Left and right dummy nodes point at each other:
        self.left = LRUNode(0, 0) # Left = least recently used
        self.right = LRUNode(0, 0) # Right = most recently used
        self.left.next = self.right
        self.right.prev = self.left

    # Helper function to remove node from linked list
    def remove(self, entry):
        prev, nxt = entry.prev, entry.next
        prev.next, nxt.prev = nxt, prev

    # Helper function to insert node at right of list (MRU):
    def insert(self, entry):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = entry
        entry.prev, entry.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache: # remove and insert to make entry MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # If new entry with same key, overwrite the old and make MRU
            self.remove(self.cache[key])
        self.cache[key] = LRUNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity: # If no capacity, delete LRU entry.
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


print("")
lRUCache = LRUCache(2)
lRUCache.put(1, 1)      # cache is {1=1}
lRUCache.put(2, 2)      # cache is {1=1, 2=2}
print(lRUCache.get(1))  # return 1
lRUCache.put(3, 3)      # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2))  # returns -1 (not found)
lRUCache.put(4, 4)      # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))  # return -1 (not found)
print(lRUCache.get(3))  # return 3
print(lRUCache.get(4))  # return 4

print("")
lRUCache = LRUCache(2)
lRUCache.put(2, 1)
lRUCache.put(2, 2)
print(lRUCache.get(2))
lRUCache.put(1, 1)
lRUCache.put(4, 1)
print(lRUCache.get(2))

print("")
lRUCache = LRUCache(1)
lRUCache.put(2, 1)
print(lRUCache.get(2))