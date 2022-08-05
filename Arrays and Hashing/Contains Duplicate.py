from operator import truediv

class Solution(object):
    def containsDuplicateUsingSorting(self, nums: list[int]) -> bool:
        # Comparing every element against every other element would be complexity O(n^2).
        # Sorting the list first has complexity O(nlogn) and reduces the problem to comparing adjacent elements.
        # Space complexity is O(1).
        nums.sort()
        l = len(nums)
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

    def containsDuplicateUsingHash(self, nums: list[int]) -> bool:
        # Inserting the elements into a hashset and checking if they already exists is even better with complexity O(n).
        # The trade off is that space complexity is O(n) since we have to create a hashmap.
        hashSet = set()
        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False
    

def testSolution(nums):
    print(nums)
    sol = Solution
    result = sol.containsDuplicateUsingSorting(sol,nums)
    print("Sorting method: " + str(result))
    result = sol.containsDuplicateUsingHash(sol,nums)
    print("Hashmap method: " + str(result))

testSolution([1,2,3])
testSolution([1,2,3,1])