from typing import List


class Solution:
    # Solution using hashset and a bit of math.
    # We can find the missing value by creating a set of numbers from 1 to n
    # and finding the set difference compared to a set of the input numbers.
    # We then calculate the expected sum using the arithmetic series formula,
    # and the actual sum of the input numbers by adding them up.
    # Since there is a value which is duplicated and another which has been replaced,
    # the difference between these must be the same as the difference between the 
    # expected sum and the actual sum.
    # We can use this to calculate the duplicated value from the missing value.
    # Ex: [1,2,2,4]:
    # expected sum = 10 (1+2+3+4)
    # actual sum = 9 (1+2+2+4)
    # sum difference = 10 - 9 = 1
    # missing value = 3
    # duplicated value = 3 - 1 = 2
    # If 3 had replaced 1, the sum difference would be 10 - 8 = 2
    # resulting in duplicated value 3 - 2 = 1
    #
    # O(n) time because there is no need to sort.
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashset = set(range(1, len(nums) + 1))
        missing = hashset.difference(set(nums)).pop()
        expectedSum = (len(nums) * (len(nums) + 1)) // 2
        duplicated = missing - (expectedSum - sum(nums))
        return [duplicated, missing]

    # Simpler solution for finding the duplicated number based
    # on removing the input numbers from the set until a number not in the set is found.
    # This is the duplicated number, which cannot be removed twice.
    # Still O(n) but not as efficient.
    def findErrorNumsNoMath(self, nums: List[int]) -> List[int]:
        hashset = set(range(1, len(nums) + 1))
        missing = hashset.difference(set(nums)).pop()
        for n in nums:
            if n not in hashset:
                duplicated = n
                break
            hashset.remove(n)
        return [duplicated, missing]

    

sol = Solution()
print(sol.findErrorNums(nums = [1,2,2,4]))
print(sol.findErrorNums(nums = [1,1]))
print(sol.findErrorNums(nums = [1,3,3]))
print(sol.findErrorNums(nums = [3,2,2]))
print("")
print(sol.findErrorNumsNoMath(nums = [1,2,2,4]))
print(sol.findErrorNumsNoMath(nums = [1,1]))
print(sol.findErrorNumsNoMath(nums = [1,3,3]))
print(sol.findErrorNumsNoMath(nums = [3,2,2]))