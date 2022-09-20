from typing import List
import collections

class Solution:
    # Make dictionary mapping numbers to set of indices with those numbers.
    # For each number, check if it is already mapped, and if one of those indices
    # is closer than k.
    # To avoid repeated comparisons, more distant values are removed from the set.
    # This works because i is always moving further away.
    def containsNearbyDuplicateSet(self, nums: List[int], k: int) -> bool:
        hashmap = collections.defaultdict(set)
        for i, n in enumerate(nums):
            if n in hashmap:
                rem = set()
                for v in hashmap[n]:
                    if i - v <= k:
                        return True
                    else:
                        rem.add(v)
                hashmap[n] - rem
            hashmap[n].add(i)
        return False

sol = Solution()
print(sol.containsNearbyDuplicateSet(nums = [1,2,3,1], k = 3))
print(sol.containsNearbyDuplicateSet(nums = [1,0,1,1], k = 1))
print(sol.containsNearbyDuplicateSet(nums = [1,2,3,1,2,3], k = 2))