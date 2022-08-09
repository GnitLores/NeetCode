import heapq

class Solution(object):
    # Solution using dictionary and heap.
    # Count occurrences of each number with dictionary.
    # Turn into list of tuples with count as first element.
    # Heapify tuples.
    # All of this is O(n) time.
    # Get k greatest counts from heap and return corresponding numbers. O(k*logm) where m is distinct numbers in array.
    # Should be very efficient unless k is large.
    def topKFrequent(self, nums, k):
        counts = dict()
        for n in nums:
            counts[n] = 1 + counts.get(n, 0) # Add one to existing count or 0 if no existing count.

        self.heap = []
        for c in counts:
            self.heap.append((counts[c]*-1, c)) # Invert to make minheap act as maxheap
        heapq.heapify(self.heap)

        return [heapq.heappop(self.heap)[1] for _ in range(k)] # Pop value of k greatest counts.

    # More efficient O(n) solution using dictionary and bucket sort.
    # Just as before, count occurences.
    # Sort values by their occurences.
    # We know that numbers cannot occur more than n times.
    # So we can make an array from zero to n with the index corresponding to the count.
    # Add a list of numbers the the element of the list corresponding to the count of those numbers..
    def topKFrequentBucket(self, nums, k):
        counts = dict()
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            counts[n] = 1 + counts.get(n, 0) # Add one to existing count or 0 if no existing count.
        for n, c in counts.items():
            freq[c].append(n)
        
        # Iterate backwards and get k largest numbers:
        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

def testSolution(*args):
    sol = Solution()
    res = sol.topKFrequent(*args)
    print(res)
    res = sol.topKFrequentBucket(*args)
    print(res)

testSolution([2,3,4,1,4,0,4,-1,-2,-1], 2)
testSolution([4,4,4,4,4,1,1,1,2,2,3,5,5,5,5,5,5,5,5], 2)
testSolution([1,1,1,2,2,3], 2)
testSolution([1], 1)

