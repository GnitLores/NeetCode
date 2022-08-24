from typing import List
import math

class Solution:
    # Not a dynamic programming solution.
    #
    # Observation: If there occurs a zero, including it makes the entire product zero.
    # Consequently, we can split the problem into two subproblems: max(0, max_left, max_right).
    # If we do this for all zeros, we can split the problem into a series of smaller subproblems
    # that are more simple because the cannot contain zero.
    # This is still linear time.
    # 
    # Assume subproblem with no zeros:
    # Observation: If there is an even number of negatives, the output is the product of the entire array.
    # If there is an odd number of negatives, we can exlcude either the leftmost or rightmost negative
    # and calculate the product to the left and right. This will always have an even number of negatives.
    # So for an odd number of negatives: max_prod = max(max_leftmost_left, max_leftmost_right, max_rightmost_left, max_rightmost_right).
    #
    # So break the problem into smaller problems without zeros, and then find max(0, max_subset).
    # This is O(n) time and space. The code is not very elegant, but the idea is simple and it is very efficient when testing on leetcode.
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        # Function for solving subproblem that has no zeroes
        def findMaxZeroless(nums):
            if len(nums) == 1: return nums[0]

            # Count negative numbers and find leftmost and rightmost negative number
            nNeg = 0
            firstNeg = -1
            lastNeg = -1
            maxProd = math.prod(nums)
            for i, n in enumerate(nums):
                if n < 0:
                    if nNeg == 0: firstNeg = i
                    lastNeg = i
                    nNeg += 1

            if nNeg % 2 == 0:   # Even number of negative numbers
                return maxProd
            else:               # odd number of negative numbers
                if firstNeg > 0:
                    maxProd = max(maxProd, math.prod(nums[0:firstNeg]))
                if firstNeg < len(nums) - 1:
                    maxProd = max(maxProd, math.prod(nums[firstNeg+1:len(nums)]))
                if nNeg >= 3:
                    if lastNeg > 0:
                        maxProd = max(maxProd, math.prod(nums[0:lastNeg]))
                    if lastNeg < len(nums) - 1:
                        maxProd = max(maxProd, math.prod(nums[lastNeg+1:len(nums)]))
            return maxProd
        
        # Break problem into smaller subproblems without zeros
        subs = []
        l = 0
        for i, n in enumerate(nums):
            if n == 0:
                if i > 0 and i > l:
                    subs.append(nums[l:i])
                l = i + 1
        if l < len(nums):
            subs.append(nums[l:])
        
        # Find max of 0 and all subproblems
        maxProd = 0
        for sub in subs:
            maxProd = max(maxProd, findMaxZeroless(sub))
        return maxProd

    # Neetcode solution.
    # This can also be solved with much less code like this.
    # Keep track of both maximal and also minimal product so far.
    # Adding the number itself as a third element in the max and min operations allows
    # us to reset the product when passing over a zero.
    # This is very elegant, but the idea is kind of abstract and would be very difficult
    # to arrive at in a short amount of time.
    # It also runs less efficiently on leetcode and has the same time complexity.
    # O(n) time but O(1) space.
    def maxProductSimple(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:

            tmpMax = curMax * n
            tmpMin = curMin * n
            curMax = max(tmpMax, tmpMin, n)
            curMin = min(tmpMax, tmpMin, n)
            res = max(res, curMax)
        return res

sol = Solution()
print(sol.maxProductSimple([5,10,0,-2,2,3,-2,4,-2,2,0,4]))
print(sol.maxProductSimple([5,10,-2,2,3,-2,4,-2,2,4]))
print(sol.maxProductSimple([2,3,-2,4]))
print(sol.maxProductSimple([2,3,4,-2]))
print(sol.maxProductSimple([-2,2,3,4]))
print(sol.maxProductSimple([-2,0,-1]))
print("")
print(sol.maxProduct([5,10,0,-2,2,3,-2,4,-2,2,0,4]))
print(sol.maxProduct([5,10,-2,2,3,-2,4,-2,2,4]))
print(sol.maxProduct([2,3,-2,4]))
print(sol.maxProduct([2,3,4,-2]))
print(sol.maxProduct([-2,2,3,4]))
print(sol.maxProduct([-2,0,-1]))