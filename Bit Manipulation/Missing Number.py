class Solution(object):
    # Easy solution using hashing.
    # O(n) time and O(n) space.
    def missingNumber(self, nums):
        hashset = set(nums)
        for n in range(0, len(nums)+1):
            if n not in hashset:
                return n
    
    # Solution using binary manipulation.
    # The order in which you xor a list of numbers does not change result.
    # Using xor on two identical numbers gives 0
    # Using xor on 0 and a number gives the number unchanged.
    # Using xor an all input numbers as well as the full sequence gives missing number.
    # O(n) time and O(1) space.
    def missingNumberBinary(self, nums):
        missing = 0
        for n in nums:
            missing = missing ^ n
        for n in range(0, len(nums) + 1):
            missing = missing ^ n
        return missing

    # Solution using sums:
    # The difference between the sum of the input and the sum of the full sequence
    # is the missing number.
    # Use the iterator to sum up the differences.
    def missingNumberSums(self, nums):
        missing = len(nums) # Initialize to the final number in the full sequence.
        for i in range(len(nums)):
            missing += (i - nums[i])
        return missing

def testSolution(*args):
    sol = Solution()
    print(sol.missingNumber(*args))
    print(sol.missingNumberBinary(*args))
    print(sol.missingNumberSums(*args))

testSolution([3,0,1])
testSolution([0,1])
testSolution([9,6,4,2,3,5,7,0,1])